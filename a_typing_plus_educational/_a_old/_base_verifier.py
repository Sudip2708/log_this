from typing import Any, Optional, Union
from abc import ABC, abstractmethod

from .._exceptions import VerifyError

class VerifyNotImplementedAttributeError(VerifyError):
    """Výjimka vyvolaná při neplatném typu hodnoty."""

    title = "\n⚠ ZACHYCENa TŘÍDA S CHYBĚJÍCÍMI POVYNNÝMI ATRIBUTY!\n"

    def __init__(self, cls_name, missing):
        self.cls_name = cls_name
        self.missing = missing

        what_happened = [
            f"   - Při inicializci byla zachycena validační třía, která nemá definovaná všechny potřebné atributy.\n"
            f"   - Jméno třídy: {self.cls_name}\n",
            f"   - Očekávaná annotace: {format_missing(REQUIRED_ATTRIBUTES)}\n",
            f"   - Chybějící atributy: {format_missing(self.missing)}\n"
        ]

        what_to_do = [
            "   - Zkontroluj definici dané třídy a doplň chybějící atributy.\n",
            "   - Pokud se tato chyba vyskytla v produkci, pravděpodobně se jedná"
            " o poškození internáích dat a je potřeba knihovnu přeinstalovat.\n"
        ]

        super().__init__(what_happened, what_to_do)


REQUIRED_ATTRIBUTES = (
    "VALIDATOR_KEY",
    "ANNOTATION",
    "IS_INSTANCE",
    "DUCK_TYPING",
    "DESCRIPTION",
    "LONG_DESCRIPTION"
)

def attributes_check(cls):
    """
    Funkce pro kontrolu poviných atributů.

    Je definvaná mimo třídu, aby zbytečně nezatěžovala potomky.
    """
    missing = [attr for attr in REQUIRED_ATTRIBUTES if not hasattr(cls, attr)]
    if missing:
        raise VerifyNotImplementedAttributeError(cls.__name__, missing)



class BaseValidator(ABC):
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
    IS_INSTANCE: Any = None
    DUCK_TYPING: Optional[str] = None
    DESCRIPTION: Optional[str] = None
    LONG_DESCRIPTION: Optional[str] = None

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
        attributes_check(cls)

    @abstractmethod
    def __call__(
        self,
        value: Any,
        annotation: Any,
        custom_types: dict = None,
        inner_check: Union[bool, int] = True,
        duck_typing: bool = False,
        bool_only: bool = False
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
