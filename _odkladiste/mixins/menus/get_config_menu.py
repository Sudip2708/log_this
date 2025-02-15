from abc import ABC
from mixins.handlers import HandlersMixin


class GetConfigMenuMixin(HandlersMixin, ABC):

    def get_config_menu(self):
        title = "▼ VYBERTE ÚKON: "
        items = [
            ("Nastavit hodnotu 1", self.switch_to_select_key),
            ("Nastavit hodnotu 2", self.set_value_handler),
            ("Nastavit hodnotu 3", self.set_value_handler),
            ("Zpět do hlavního menu", self.switch_to_main)
        ]
        return title, items
