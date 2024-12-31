from threading import local
from .mixins import (
    IncreaseDepthAndUpdateTypeMixin,
    DecreaseDepthMixin,
)


class ThreadContext(
    IncreaseDepthAndUpdateTypeMixin,
    DecreaseDepthMixin,
):
    """
    Singleton třída spravující vlákno pro logování.

    Mixins:
        IncreaseDepthAndUpdateTypeMixin: Navýší hloubku zanoření a zaznamená hodnotu mode.
        DecreaseDepthMixin: Sníží hodnotu hloubky zanoření.
        PropertyMixin: Přidává property pro přímí přístup k hodnotám vlákna.

    Attributes:
        _instance: Singleton instance pro správu vlákna.
    """

    # Atribut pro singleton instanci třídy:
    _instance = None

    # Vytvoření instance:
    def __new__(cls):
        """
        Implementace singleton vzoru.

        Metoda nejprve zjistí, zda již není vytvořena instance.
        Pokud není, pak instanci vytvoří, a zároveň i vytvoří atribut
        odkazující na instancí třídy local z modulu threading,
        kde se budou uchovávat další všechny informce.
        Pokud instance je již vytvořena, vrací vytvořenou instanci.

        Returns:
            ThreadContext: Singleton instance pro správu vlákna
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.thread = local()
        return cls._instance

    # Základní inicializace instance
    def __init__(self):
        """
        Nastaví kontext vlákna na výchozí hodnoty.

        Metoda nejprve překontroluje, zda je již instance inicializovaná.
        Pokud ne, pak smaže obsah vnitřního slovníku atributu thread.
        Dále uvnitř atributu pro instanci třídy local vytvoří atributy
        pro záznam hloubky a typu modu.
        Metoda následně nastaví atribut potvrzující proběhlou inicializaci.

        """
        # Kontrola zda instance ještě není inicializovaná
        if not hasattr(self, '_initialized'):

            # Smazání případného obsahu
            self.thread.__dict__.clear()

            # Přiřazení atributů
            self.thread.current_depth = -1
            self.thread.last_depth = 0
            self.thread.current_type = 0
            self.thread.last_type = 0

            # Záznam o provedení inicializace
            self._initialized = True

    @property
    def current_depth(self):
        return self.thread.current_depth

    @current_depth.setter
    def current_depth(self, value):
        if not isinstance(value, int):
            raise TypeError("Current depth must be an integer")
        if value < -1:  # Assuming -1 is your minimum valid depth
            raise ValueError("Current depth cannot be less than -1")
        self.thread.current_depth = value

    @property
    def last_depth(self):
        return self.thread.last_depth

    @last_depth.setter
    def last_depth(self, value):
        self.thread.last_depth = value

    @property
    def current_type(self):
        return self.thread.current_type

    @current_type.setter
    def current_type(self, value):
        if not isinstance(value, int):
            raise TypeError("Current type must be an integer")
        if value < 0:
            raise ValueError("Current type cannot be negative")
        self.thread.current_type = value

    @property
    def last_type(self):
        return self.thread.last_type

    @last_type.setter
    def last_type(self, value):
        self.thread.last_type = value


