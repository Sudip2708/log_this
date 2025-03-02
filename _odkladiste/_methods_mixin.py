from abc import ABC

from abc_helper import abc_property
from cli_styler import print_styled_success_title


class ResponseManagerMethodMixin(ABC):
    """Definice metod pro správu reakcí"""

    # Atribut pro instanci hlavní třídy
    cli = abc_property("cli")

    # Atribut pro definice akcí
    response_actions = abc_property("response_actions")

    def get_response(self):
        """Vrací výstupní reakci na daný požadavek"""
        action = self.response_actions.get(self.cli.response)
        if action:
            action()
            self.cli.response = None  # Reset odpovědi


    def print_new_settings(self):
        """Tiskne aktuálně změněnou hodnotu"""
        print_styled_success_title(
            f"Vybrán klíč: {self.cli.selected_key}, "
            f"hodnota: {self.cli.selected_value}"
        )
        print()
        self.cli.selected_key = None
        self.cli.selected_value = None


