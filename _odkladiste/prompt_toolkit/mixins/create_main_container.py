class CreateMainContainerMixin:

    def create_main_container(self):
        """
        Vytvoří hlavní rozložení aplikace.

        Returns:
            HSplit: Rozložení aplikace.
        """
        self.key_label = Label(f"Key: {self.key_list[self.current_key_index]}")
        self.value_buttons = self.create_value_buttons(self.key_list[self.current_key_index])

        return HSplit([
            self.key_label,
            Box(HSplit(self.value_buttons), padding=1),
            self.message,
        ])
