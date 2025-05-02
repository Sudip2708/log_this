from typing import Final

from ....._bases import BaseCustomLogicValidator, T
from ....._verifiers import inner_args_transmitter


class FinalValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci Final[T]

    Final je typová anotace, která označuje, že proměnná nesmí být přeřazena po své
    inicializaci. Slouží jako indikátor konstanty pro statické analyzátory typu, ale
    na samotnou runtime validaci hodnoty nemá vliv. Pro účely validace se ověřuje
    pouze vnitřní typ T.

    Syntaxe:
        - Final[T]              # T je vnitřní typ proměnné
        - Final                 # Bez specifikace typu (ekvivalent Final[Any])

    Příklady použití:
        - Final[int]           # Konstanta typu int
        - Final[List[str]]     # Neměnná reference na seznam řetězců
        - Final                # Konstanta bez specifikace typu
        - X: Final = 42        # Konstanta bez explicitního typu (odvození z hodnoty)

    Validační proces:
        1. Získání vnitřního typu T z anotace Final[T]
        2. Rekurzivní validace hodnoty vůči vnitřnímu typu T
        3. Final samotný nepřidává žádné další validační podmínky na hodnotu

    Použití v kódu:
        ```python
        # Na úrovni modulu
        VERSION: Final = "1.0.0"
        MAX_RETRIES: Final[int] = 3

        class Config:
            # Třídní konstanty
            DEBUG: Final[bool] = True

            # Instanční konstanty
            def __init__(self, host: str):
                self.HOST: Final[str] = host
        ```

    Specifické informace:
        - Od Python 3.8: Final byl představen v PEP 591 a je k dispozici od Pythonu 3.8
        - Vztah ke konstantám: Final je způsob, jak v Pythonu označit konstanty, které
          jsou v jiných jazycích definovány klíčovým slovem const
        - Kombinace s ClassVar: Lze kombinovat jako ClassVar[Final[int]] pro neměnné
          třídní atributy
        - Kontrola validátory: Statické analyzátory jako mypy detekují pokusy o přepsání
          Final proměnných a signalizují chybu
        - Runtime význam: Final má význam pouze při typové kontrole, při běhu nemá efekt

    Běžné chyby:
        - Nesprávné pochopení: Final nezajišťuje skutečnou neměnnost, pouze označuje záměr
        - Mutace obsahu: Final zabraňuje pouze přeřazení, ale obsah mutable objektů
          lze stále měnit (např. seznam v Final[List[int]])
        - Použití s typovými aliasy: Final nelze použít s typovými aliasy (např. `type X = Final[int]`)
        - Záměna s konstantami: Final není automatický převod na skutečně neměnný objekt

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Final
        - https://peps.python.org/pep-0591/ (Adding a final qualifier to typing)
        - https://mypy.readthedocs.io/en/stable/final_attrs.html
    """

    VALIDATOR_KEY = "final"
    ANNOTATION = Final[T]

    IS_INSTANCE = Final
    HAS_ATTRS = None  # Nepodporuje validaci přes Duck Typing.
    CALLABLE_ATTRS = None  # Nepodporuje validaci přes Duck Typing.

    DESCRIPTION = "Neměnný symbol"
    LONG_DESCRIPTION = (
            "Validuje, že proměnná nebo metoda je označena jako Final, "
            "tedy že by neměla být přepisována nebo přetěžována v podtřídách."
        )

    def __call__(self, value, annotation, depth_check, custom_types,
                 bool_only):
        """Definice metody __call__ pro přeformulování dotazu.

        Předává validaci vnitřnímu typu anotace Final.
        """
        return inner_args_transmitter(
            value, annotation, depth_check, custom_types, bool_only
        )