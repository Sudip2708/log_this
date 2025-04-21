class ConditionIfMixins:

    def _condition_if(self, words):
        """Zpracování podmínky 'if'."""
        condition_words = words[1:]

        if len(condition_words) >= 2 and condition_words[0] == "value":
            # Podmínka na hodnotu, např. "if value current speed"
            value_name = "_".join(condition_words[1:])
            self.current_context.append(("if", value_name))
            return {"condition": "if", "value": value_name}
        else:
            # Obecná podmínka
            condition = " ".join(condition_words)
            self.current_context.append(("if", condition))
            return {"condition": "if", "raw_condition": condition}

