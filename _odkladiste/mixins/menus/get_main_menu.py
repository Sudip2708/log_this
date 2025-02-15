from abc import ABC
from mixins.handlers import HandlersMixin


class GetMainMenuMixin(HandlersMixin, ABC):

    def get_main_menu(self):
        title = "▼ VYBERTE ÚKON: "
        items = [
            ("Nápověda", self.show_help_handler),
            ("Zobrazit konfiguraci", self.show_config_handler),
            ("Nastavit konfiguraci", self.switch_to_config_menu),
            ("Ukončit", self.exit_handler)
        ]
        return title, items
