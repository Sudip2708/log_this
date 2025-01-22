class SetValueMixin:

    def set_value(self, value):
        """
        Nastaví vybranou hodnotu.

        Args:
            value (str): Hodnota k nastavení.
        """
        self.selected_value = value
        self.message.text = f"Selected value: {value}"
