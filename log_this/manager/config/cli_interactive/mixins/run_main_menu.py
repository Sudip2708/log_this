from abc import ABC, abstractmethod
from ._main_menu_picker import MainMenuPickerMixin
from typing import Optional, Any


class RunMixin(MainMenuPickerMixin, ABC):

    @staticmethod
    @abstractmethod
    def show_help() -> None:
        """Zobrazí nápovědu pro používání interaktivního režimu."""
        pass

    @abstractmethod
    def run_config_settings(self) -> None:
        """Zpracuje proces změny konfigurace."""
        pass

    @staticmethod
    @abstractmethod
    def _exit_interactive_mode(message: Optional[str] = None) -> None:
        """Ukončí interaktivní režim s volitelnou zprávou."""
        pass

    def run_main_menu(self) -> None:
        """Spustí interaktivní režim a zobrazí hlavní menu."""

        # Intro
        print("\nVítejte v interaktivním režimu konfigurace LogThis!")

        # Cyklus pro hlavní menu
        while True:

            # Načtení vstupu z hlavního menu
            result = self._main_menu_picker()

            # Pokud byl zadán požadavek na změnu konfigurace
            if result == 'config':
                # Volání metody pro změnu konfigurace
                self.run_config_settings()

            # Pokud byl zadán požadavek na nápovědu
            elif result == 'help':
                # Volání metody pro nápovědu
                self.show_help()

            # Pokud byl zadán požadavek na ukončení interaktivního režimu
            if result == 'exit':
                # Volání metody pro ukončení interaktivního režimu
                self._exit_interactive_mode()
                break


