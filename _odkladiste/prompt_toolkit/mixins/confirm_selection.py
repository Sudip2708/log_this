class ConfirmSelectionMixin:

    def confirm_selection(self, _):
        """
        Potvrdí aktuální výběr klíče a hodnoty.
        """
        self.selected_key = self.key_list[self.current_key_index]
        if self.selected_value:
            self.message.text = f"Confirmed: {self.selected_key} = {self.selected_value}"
        else:
            self.message.text = "Error: No value selected!"
