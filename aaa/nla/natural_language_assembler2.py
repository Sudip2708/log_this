from action_manager import ActionManager

class NaturalLanguageAssembler:
    """
    Základní třída jazyku
    """

    def __init__(self):

        # Vytvoření slovníku pro definovaání vlastních objetů
        self.objects = {}
        self.action_manager = ActionManager()
        self.action_manager.set_objects(self.objects)
        self.actions = self.action_manager.get_actions_dict()


    def parse_text(self, text):
        """Zpracování celého textu a jeho rozdělení na věty."""
        sentences = []
        current_sentence = ""

        i = 0
        while i < len(text):
            if text[i:i + 2] == ". " or text[i:i + 2] == ".\n":
                current_sentence += text[i]
                sentences.append(current_sentence.strip())
                current_sentence = ""
                i += 2
            else:
                current_sentence += text[i]
                i += 1

        # Přidání poslední věty, pokud existuje
        if current_sentence.strip():
            sentences.append(current_sentence.strip())

        return self.process_sentences(sentences)

    def process_sentences(self, sentences):
        """Zpracování jednotlivých vět."""
        results = []

        for sentence in sentences:
            # Rozdělení věty na souvětí
            clauses = self.split_into_clauses(sentence)

            # Zpracování každého souvětí
            processed_clauses = []
            for clause in clauses:
                words = self.split_into_words(clause)
                processed = self.process_words(words)
                processed_clauses.append(processed)

            results.append({
                "sentence": sentence,
                "clauses": clauses,
                "processed": processed_clauses
            })

        return results

    def split_into_clauses(self, sentence):
        """Rozdělení věty na souvětí dle čárky s mezerou za ní."""
        clauses = []
        current_clause = ""

        i = 0
        while i < len(sentence):
            if sentence[i:i + 2] == ", ":
                current_clause += sentence[i]
                clauses.append(current_clause.strip())
                current_clause = ""
                i += 2
            else:
                current_clause += sentence[i]
                i += 1

        # Přidání posledního souvětí, pokud existuje
        if current_clause.strip():
            clauses.append(current_clause.strip())

        return clauses

    def split_into_words(self, clause):
        """Rozdělení souvětí na slova."""
        # Odstranění interpunkce na konci
        clause = clause.rstrip('.,:;!?')
        # Rozdělení podle mezer
        words = [word.lower() for word in clause.split()]
        return words

    def process_words(self, words):
        """Zpracování slov a hledání akcí ve slovníku."""
        i = 0
        result = {}

        while i < len(words):
            word = words[i]
            action_found = False

            # Hledání v slovníku akcí
            if word in self.actions:
                action = self.actions[word]

                # Kontrola, zda je akce slovník (může potřebovat další slovo)
                if isinstance(action, dict) and i + 1 < len(words):
                    next_word = words[i + 1]
                    if next_word in action:
                        # Našli jsme dvojici slov ve slovníku
                        result_action = action[next_word](words[i:])
                        result[f"{word}_{next_word}"] = result_action
                        action_found = True
                        i += 2  # Přeskočíme obě slova

                # Pokud není slovník nebo jsme nenašli další slovo
                if not action_found and callable(action):
                    result_action = action(words[i:])
                    result[word] = result_action
                    action_found = True
                    i += 1  # Přeskočíme jedno slovo

            if not action_found:
                # Pokud nenajdeme akci, prostě slovo přidáme
                result[f"word_{i}"] = word
                i += 1

        return result

    def compile(self, text):
        """Kompilace textu do vnitřní reprezentace objektů."""
        parsed_result = self.parse_text(text)

        # Tady by následovala logika pro kompilaci do finálních objektů
        # Pro demonstraci vrátíme aktuální stav objektů a zpracovaný text
        return {
            "parsed": parsed_result,
            "objects": self.objects
        }

    def generate_python(self):
        """Generování Python kódu z vnitřní reprezentace objektů."""
        result = []

        for obj_name, obj_data in self.objects.items():
            # Základní definice funkce
            function_def = f"def {obj_name}("

            # Parametry funkce
            params = []
            param_types = []
            if "expect" in obj_data:
                for param_name, param_data in obj_data["expect"].items():
                    params.append(param_name)
                    if "type" in param_data:
                        type_str = " | ".join(
                            [t.__name__ for t in param_data["type"]])
                        param_types.append(f"{param_name}: {type_str}")

            if param_types:
                function_def += ", ".join(param_types)
            else:
                function_def += ", ".join(params)

            function_def += "):"
            result.append(function_def)

            # Tělo funkce - toto by byl složitější proces, tady je jen zjednodušený příklad
            # Implementace pro ukázkový příklad "speed_up"
            if obj_name == "speed_up" and "expect" in obj_data and "current_speed" in \
                    obj_data["expect"]:
                result.append("    if current_speed:")
                result.append("        print(current_speed + 10)")
                result.append("    else:")
                result.append(
                    '        print("Current speed was not specified.")')
            else:
                result.append("    pass")

            result.append("")  # Prázdný řádek mezi funkcemi

        return "\n".join(result)
