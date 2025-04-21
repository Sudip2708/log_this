class ActionPrintMixins:

    def _action_print(self, words):
        """Zpracování akce 'print'."""
        # Následující slova po 'print' určují, co se má vytisknout
        content_words = words[1:]

        if len(content_words) >= 2 and content_words[0] == "value":
            # Je to tisk hodnoty, např. "print value current speed"
            value_name = "_".join(content_words[1:])

            # Kontrola, zda následuje operace
            plus_index = -1
            for i, word in enumerate(content_words):
                if word == "plus":
                    plus_index = i
                    break

            if plus_index > 0:
                # Máme operaci, např. "print value current speed plus ten"
                value_name = "_".join(content_words[1:plus_index])
                operation = content_words[plus_index]
                operand = content_words[plus_index + 1]

                # Převod slovních čísel na hodnoty
                number_map = {"ten": 10, "twenty": 20, "thirty": 30}
                operand_value = number_map.get(operand, operand)

                return {
                    "action": "print",
                    "value": value_name,
                    "operation": operation,
                    "operand": operand_value
                }
            else:
                return {"action": "print", "value": value_name}
        elif len(content_words) >= 1 and content_words[0] == "text":
            # Je to tisk textu, např. "print text current speed was not specified"
            text = " ".join(content_words[1:])
            return {"action": "print", "text": text}
        else:
            # Obecný tisk
            content = " ".join(content_words)
            return {"action": "print", "content": content}

