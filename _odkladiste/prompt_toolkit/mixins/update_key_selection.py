class UpdateKeySelectionMixin:

    def update_key_selection(self):
        """
        Aktualizuje zobrazení při změně klíče.
        """
        self.key_label.text = f"Key: {self.key_list[self.current_key_index]}"
        self.value_buttons = self.create_value_buttons(self.key_list[self.current_key_index])
        self.layout.container = self.create_main_container()
