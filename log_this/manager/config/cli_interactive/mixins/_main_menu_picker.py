from abc import ABC, abstractmethod
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import radiolist_dialog


class MainMenuPickerMixin(ABC):

    @property
    @abstractmethod
    def style(self) -> Style:
        """Atribut s nastavením stylu vzhledu."""
        pass


    def _main_menu_picker(self) -> str:
        """
        Zobrazí hlavní menu s možnostmi výběru.

        Returns:
            str: Klíč vybrané akce
        """

        # Vytvoření pickeru
        return radiolist_dialog(
            title='Hlavní menu',
            text='Vyberte požadovaný úkon:',
            values=[
                ('config', 'Změnit konfiguraci'),
                ('help', 'Zobrazit nápovědu'),
                ('exit', 'Ukončit interaktivní režim')
            ],
            style=self.style
        ).run()