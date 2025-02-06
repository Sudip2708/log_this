from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Dict, Union
from collections import deque


class SaveToHistoryMixin(ABC):
    """Mixin pro správu historie konfigurace pomocí snapshotů."""

    @abstractmethod
    @property
    def config(self) -> Dict[str, Union[int, str, bool]]:
        """Atribut se slovníkem s aktuálními hodnotami"""
        pass

    @abstractmethod
    @config.setter
    def config(self, config_dict: Dict[str, Union[int, str, bool]]) -> None:
        """Atribut se slovníkem s aktuálními hodnotami"""
        pass

    @abstractmethod
    @property
    def _history(self) -> deque[Dict[str, Union[int, str, bool]]]:
        """Atribut se seznamem historických snapshotů."""
        pass


    def save_settings_to_history(self):
        """Uloží aktuální konfiguraci jako snapshot."""

        # Vytvoření kopie aktuální konfigurace
        snapshot = deepcopy(self.config)

        # Uložení do atributu
        self._history.append(snapshot)

