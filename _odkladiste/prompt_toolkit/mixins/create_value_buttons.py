class CreateValueButtonsMixin:

    def create_value_buttons(self, key):
        """
        Vytvoří tlačítka pro výběr hodnot podle aktuálního klíče.

        Args:
            key (str): Aktuální klíč.

        Returns:
            list: Seznam tlačítek.
        """
        values = self.options[key]
        return [Button(text=value, handler=lambda v=value: self.set_value(v)) for value in values]
