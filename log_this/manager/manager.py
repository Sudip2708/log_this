from .logger import log_this_logger
from .config import config
from .thread import thread
from .serializer import serializer
from .methods import (
    GetIndentMethodMixins,
    GetBlankLinesMethodsMixins,
    GetLimitedDocstringMixin
)


class LogThisManager(
    GetIndentMethodMixins,
    GetBlankLinesMethodsMixins,
    GetLimitedDocstringMixin
):
    """
    Singleton třída pro správu knihovny.

    Mixins:
        GetIndentMethodMixins: Metoda pro odsazení.
        GetBlankLinesMethodsMixins: Metoda pro prázdné řádky.
        GetLimitedDocstringMixin: Metoda vrátí zkrácenou verzi docstringu na nastavený počet.

    Attributes:
        _instance: Singleton instance pro správu obsahu.
    """

    # Atribut pro instanci třídy:
    _instance = None


    # Vytvoření instance:
    def __new__(cls):
        """
        Implementace singleton vzoru.

        Vytvoří jedinou instanci konfigurace nebo vrátí existující.

        Returns:
            LogThisManager: Singleton instance pro manažera konfigurace
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


    # Základní inicializace instance
    def __init__(self):
        """
        Inicializace základních atributů pro třídu LogThisManager.

        Attributes:
            self.logger: Funkce pro nastavení loggeru
            self.config: Singleton instance pro správu konfigurace.
            self.thread: Singleton instance spravující vlákno pro logování.
            self.serialize: Třída pro serializaci objektů.
        """
        if not hasattr(self, '_initialized'):
            self.logger = log_this_logger
            self.config = config
            self.thread = thread
            self.serialize = serializer
            self.serialize.max_depth = self.config["max_depth"]
            self._initialized = True




