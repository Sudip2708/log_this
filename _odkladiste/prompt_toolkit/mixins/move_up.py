class MoveUpMixin:

    def move_up(self, _):
        """
        Posune výběr klíče nahoru.
        """
        if self.current_key_index > 0:
            self.current_key_index -= 1
            self.update_key_selection()
