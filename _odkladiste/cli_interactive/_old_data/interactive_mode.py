# log_this/manager/config/cli/interactive_mode.py
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import CompleteStyle, print_formatted_text
from prompt_toolkit.completion import WordCompleter


class InteractiveMode:
    """Třída pro interaktivní režim nastavení konfigurace."""

    def __init__(self, config):
        self.config = config

    def start(self):
        """Spustí interaktivní režim."""
        try:
            # Výběr klíče
            key = self._select_key()

            # Zadání hodnoty
            value = self._input_value(key)

            # Nastavení hodnoty
            self.config.set_new_value(key, value, value_check=True)
            print_formatted_text(f"Nastaven klíč '{key}' na hodnotu '{value}'.")

        except KeyboardInterrupt:
            print_formatted_text("Interaktivní režim přerušen uživatelem.")

    def _select_key(self) -> str:
        """Vybere klíč z dostupných možností."""
        options = [
            f"{key} - {data.INFO}"
            for key, data in self.config.keys_data.items()
        ]
        completer = WordCompleter(options, sentence=True, match_middle=True)

        key = prompt(
            "Vyberte klíč: ",
            completer=completer,
            complete_style=CompleteStyle.READLINE_LIKE,
        ).split(" - ")[0]

        return key

    def _input_value(self, key: str) -> str:
        """Zadá hodnotu pro zvolený klíč."""
        key_data = self.config.keys_data[key]
        print_formatted_text(key_data.DETAIL)

        # Cyklus kontrolující zadání správné hodnoty
        while True:
            try:
                value = prompt(f"Zadejte hodnotu pro '{key}': ")
                self.config.validate_value(key, value)  # Ověření výběru
                break
            except ValueError as e:
                print_formatted_text(f"Chyba: {e}. Zkuste to znovu.")
            except KeyboardInterrupt:
                print_formatted_text("Zadávání přerušeno uživatelem.")
                raise
        return value
