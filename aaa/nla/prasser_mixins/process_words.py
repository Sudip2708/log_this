class ProcessWordsMixins:

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