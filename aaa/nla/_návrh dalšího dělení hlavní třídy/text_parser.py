class TextParser:

    def parse_text(self, text):
        """Hlavní metoda pro zpracování celého textu."""
        sentences = self._split_into_sentences(text)
        return self.process_sentences(sentences)

    def _split_into_sentences(self, text):
        """Rozdělení textu na věty."""
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

        if current_sentence.strip():
            sentences.append(current_sentence.strip())

        return sentences

    def process_sentences(self, sentences):
        """Zpracování jednotlivých vět."""
        results = []

        for sentence in sentences:
            clauses = self._split_into_clauses(sentence)
            processed_clauses = []

            for clause in clauses:
                words = self._split_into_words(clause)
                processed = self._process_words(words)
                processed_clauses.append(processed)

            results.append({
                "sentence": sentence,
                "clauses": clauses,
                "processed": processed_clauses
            })

        return results

    def _split_into_clauses(self, sentence):
        """Rozdělení věty na souvětí."""
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

        if current_clause.strip():
            clauses.append(current_clause.strip())

        return clauses

    def _split_into_words(self, clause):
        """Rozdělení souvětí na slova."""
        clause = clause.rstrip('.,:;!?')
        words = [word.lower() for word in clause.split()]
        return words

    def _process_words(self, words):
        """Zpracování slov a hledání akcí ve slovníku."""
        i = 0
        result = {}

        # Budete muset předat slovník akcí a objektů do této metody
        actions = self.actions  # Toto bude třeba upravit
        objects = self.objects  # Toto bude třeba upravit

        while i < len(words):
            word = words[i]
            action_found = False

            # Hledání v slovníku akcí
            if word in actions:
                action = actions[word]

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


