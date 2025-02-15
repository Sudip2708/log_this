from abc import ABC
from mixins.handlers import HandlersMixin


class GetSelectKeyMenuMixin(HandlersMixin, ABC):

    def get_select_key_menu(self):
        title = "▼ VYBERTE KLÍČ: "
        items = [
            ("key_1", lambda: self.switch_to_set_key("key_1")),
            ("key_2", lambda: self.switch_to_set_key("key_2")),
            ("key_3", lambda: self.switch_to_set_key("key_3")),
            ("Zpět", self.switch_to_config_menu)
        ]
        return title, items
