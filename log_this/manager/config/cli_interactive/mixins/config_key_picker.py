from abc import ABC, abstractmethod
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.styles import Style
from typing import Optional


class ConfigKeyPickerMixin(ABC):

    @property
    @abstractmethod
    def keys_data(self) -> dict[str, Any]:
        """Atribut pro přístup k instancím klíčů ."""
        pass

    @property
    @abstractmethod
    def style(self) -> Style:
        """Atribut s nastavením stylu vzhledu."""
        pass


    def config_key_picker(self) -> Optional[str]:
        """
        Zobrazí menu pro výběr konfiguračního klíče.

        Returns:
            Optional[str]: Vybraný klíč nebo None při zrušení
        """

        # Načtení klíčů a info textu pro podrobnosti k výběru
        values = [
            (key, f"Nastavení pro '{key}' - {self.keys_data[key].info}")
            for key in self.keys_data
        ]

        # Přidání položky pro opuštění konfigurace
        values.append(('exit', 'Ukončit interaktivní režim'))

        # Vytvoření pickeru
        return radiolist_dialog(
            title='Výběr konfiguračního klíče',
            text='Vyberte klíč pro změnu hodnoty:',
            values=values,
            style=self.style
        ).run()
