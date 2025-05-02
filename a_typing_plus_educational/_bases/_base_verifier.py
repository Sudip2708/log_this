from typing import Any, Optional, Tuple, Union
from abc import ABC, abstractmethod

from .._exceptions import VerifyInternalNotImplementedError


class BaseVerifier(ABC):
    """
    Základní abstraktní třída, ze které vycházejí všechny ostatní validační třídy.

    Každá podtřída musí definovat čtyři povinné atributy:
        - VALIDATOR_KEY: Unikátní identifikátor validátoru (např. "int", "str", ...)
        - ANNOTATION: Typová anotace, na kterou se validátor vztahuje (např. `int`)
        - INFO: Popis validátoru (např. "Validátor pro typ int")
        - ORIGIN: Původní typ, se kterým validátor pracuje (např. `int`, `list`, ...)
    """

    # Povinné konstanty, které musí definovat každá koncová třída
    VALIDATOR_KEY: Optional[str] = None
    ANNOTATION: Any = None
    INFO: Optional[str] = None
    ORIGIN: Optional[type] = None

    def __init_subclass__(cls):
        """
        Kontrola povinných atributů při dědění.

        Tato metoda se automaticky spustí při vytvoření podtřídy a slouží
        ke kontrole, zda má podtřída všechny povinné atributy správně definované.

        Použití:
            Metoda __init_subclass__ umožňuje rodičovské třídě reagovat na vytvoření podtřídy,
            např. pro:
                - registraci validátorů,
                - nastavení výchozích hodnot,
                - ověření povinných atributů,
                - nebo konfiguraci chování potomka.
        """
        super().__init_subclass__()

        # Kontrola, zda jsou všechny povinné atributy definovány
        missing = [
            attr
            for attr in ("VALIDATOR_KEY", "ANNOTATION", "INFO", "ORIGIN")
            if not hasattr(cls, attr)
        ]
        if missing:
            raise VerifyInternalNotImplementedError(cls.__name__, missing)

    @abstractmethod
    def __call__(
        self,
        value: Any,
        annotation: Any,
        inner_check: Union[bool, int],
        custom_types: dict = None,
        bool_only: bool
    ) -> Union[bool, Any]:
        """
        Hlavní metoda pro definici validační logiky.

        Tato metoda musí být implementována v každé podtřídě.

        Args:
            value (Any): Hodnota, která má být ověřena.
            annotation (Any): Typová anotace očekávaného typu (např. `int`, `list[int]`).
            inner_check (Union[bool, int]): Hloubka kontroly nebo přepínač vnořených validací.
            custom_types (Tuple[Any, ...]): Uživatelsky definované typy nebo specifikace.
            bool_only (bool): Pokud je True, vrací se pouze True/False.
                               Pokud je False, při nevalidní hodnotě se vyhazuje výjimka.

        Returns:
            Union[bool, Any]: Výsledek validace:
                - `True` pokud je validace úspěšná.
                - `False` pokud není validní a `bool_only=True`.
                - Výjimka (`raise`) pokud není validní a `bool_only=False`.

        Raises:
            Výstupem může být výjimka, pokud validace selže a není nastaven `bool_only=True`,
            nebo pokud dojde k vnitřní chybě v implementaci validátoru.
        """
        pass
