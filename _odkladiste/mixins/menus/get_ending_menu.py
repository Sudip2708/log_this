from abc import ABC
from mixins.handlers import HandlersMixin


class GetEndingMenuMixin(HandlersMixin, ABC):

    def get_ending_menu(self):
        title = None
        items = [
            ("Pokračovat v interaktivním režimu", self.switch_to_main),
            ("Ukončit interaktivní režim", self.exit_handler)
        ]
        return title, items
