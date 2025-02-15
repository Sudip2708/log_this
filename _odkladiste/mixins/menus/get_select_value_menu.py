from abc import ABC
from mixins.handlers import HandlersMixin


class GetSelectKValueMenuMixin(HandlersMixin, ABC):

    def get_select_value_menu(self):
        title = f"▼ VYBERTE HODNOTU PRO {self.selected_key.upper()}: "
        items = [
            ("value_1", lambda: self.set_value_and_print("value_1")),
            ("value_2", lambda: self.set_value_and_print("value_2")),
            ("value_3", lambda: self.set_value_and_print("value_3")),
            ("Zadat vlastní hodnotu", self.input_custom_value),
            ("Zpět", self.switch_to_select_key)
        ]
        return title, items
