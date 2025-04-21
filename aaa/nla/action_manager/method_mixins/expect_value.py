class ExpectValueMixins:

    def _expect_value(self, words):
        """Zpracování akce 'expect value'."""
        if not self.current_object:
            return {"error": "No current object selected"}

        # Slova po 'expect value' reprezentují název hodnoty
        value_name_words = words[2:]
        value_name = "_".join(value_name_words)

        # Přidání očekávané hodnoty do objektu
        if "expect" not in self.objects[self.current_object]:
            self.objects[self.current_object]["expect"] = {}

        self.objects[self.current_object]["expect"][value_name] = {
            "name": tuple(value_name_words),
            "type": (int, float)  # Pro 'value' předpokládáme číselné typy
        }

        return {"expected_value": value_name}

