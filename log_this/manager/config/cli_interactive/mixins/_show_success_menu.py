from abc import ABC, abstractmethod
from prompt_toolkit.shortcuts import radiolist_dialog
from typing import Any

class ShowSuccessMenuMixin(ABC):

    @abstractmethod
    def run_main_menu(self) -> None:
        """Spustí interaktivní režim a zobrazí hlavní menu."""
        pass

    @property
    @abstractmethod
    def style(self) -> Style:
        """Atribut s nastavením stylu vzhledu."""
        pass

    def _show_success_menu(self, key: str, value: Any) -> None:
        """
        Zobrazí potvrzení o úspěšné změně a menu pro další akci.

        Args:
            key: Změněný klíč
            value: Nová hodnota
        """
        print(f"\nÚspěšně jste nastavili klíč '{key}' na hodnotu {value}")

        result = radiolist_dialog(
            title='Další akce',
            text='Vyberte další akci:',
            values=[
                ('main', 'Hlavní menu'),
                ('exit', 'Ukončit interaktivní režim')
            ],
            style=self.style
        ).run()

        if result == 'main':
            self.run_main_menu()

        if result == 'exit':
            print("\nUkončuji interaktivní režim...")
            exit(0)