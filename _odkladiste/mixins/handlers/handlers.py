from abc import ABC, abstractmethod
from mixins.handlers import (
    SwitchToMainMixin,
    SwitchToConfigMenuMixin,
    SwitchToMSelectKeyMixin,
    SwitchToSetKeyMixin,
    SetValueAndPrintMixin,
    ResetKeyValueMixin,
    InputCustomValueMixin,
    ShowHelpHandlerMixin,
    ShowConfigHandlerMixin,
    SetValueHandlerMixin,
    ExitHandlerMixin,
)

class HandlersMixin(
    SwitchToMainMixin,
    SwitchToConfigMenuMixin,
    SwitchToMSelectKeyMixin,
    SwitchToSetKeyMixin,
    SetValueAndPrintMixin,
    ResetKeyValueMixin,
    InputCustomValueMixin,
    ShowHelpHandlerMixin,
    ShowConfigHandlerMixin,
    SetValueHandlerMixin,
    ExitHandlerMixin,
    ABC
):

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def switch_menu(self, new_menu_type):
        pass

    @property
    @abstractmethod
    def show_help(self):
        pass

    @show_help.setter
    @abstractmethod
    def show_help(self, value):
        pass

    @property
    @abstractmethod
    def response(self):
        pass

    @response.setter
    @abstractmethod
    def response(self, value):
        pass

    @property
    @abstractmethod
    def selected_key(self):
        pass

    @selected_key.setter
    @abstractmethod
    def selected_key(self, value):
        pass

    @property
    @abstractmethod
    def selected_value(self):
        pass

    @selected_value.setter
    @abstractmethod
    def selected_value(self, value):
        pass

    @abstractmethod
    def get_menu_items(self, menu_type):
        pass

    @abstractmethod
    def switch_to_main(self):
        pass

    @abstractmethod
    def switch_to_config_menu(self):
        pass

    @abstractmethod
    def switch_to_select_key(self):
        pass

    @abstractmethod
    def switch_to_set_key(self, key=None):
        pass

    @abstractmethod
    def set_value_and_print(self, value):
        pass

    @abstractmethod
    def reset_key_value(self):
        pass

    @abstractmethod
    def input_custom_value(self):
        pass

    @abstractmethod
    def show_help_handler(self):
        pass

    @abstractmethod
    def show_config_handler(self):
        pass

    @abstractmethod
    def set_value_handler(self):
        pass

    @abstractmethod
    def exit_handler(self):
        pass

