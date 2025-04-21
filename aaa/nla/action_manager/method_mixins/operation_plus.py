class OperationPlusMixins:

    def _operation_plus(self, words):
        """Zpracování operace 'plus'."""
        if len(words) > 1:
            # Převod slovních čísel na hodnoty
            number_map = {"ten": 10, "twenty": 20, "thirty": 30}
            operand = words[1]
            operand_value = number_map.get(operand, operand)
            return {"operation": "plus", "operand": operand_value}
        else:
            return {"operation": "plus", "error": "Missing operand"}

