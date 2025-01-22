class MoveDownMixin:

    def move_down(self, _):
        """
        Posune výběr klíče dolů.
        """
        if self.current_key_index < len(self.key_list) - 1:
            self.current_key_index += 1
            self.update_key_selection()
