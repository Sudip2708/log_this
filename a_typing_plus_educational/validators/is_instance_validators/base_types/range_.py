from ..._bases import BaseIsInstanceValidator


class RangeValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci range

    range v Pythonu reprezentuje sekvenci čísel, která je generována pomocí
    funkce `range()`. Tato funkce vytváří sekvence čísel v určitém rozsahu, které
    mohou být iterovány, ale nemohou být změněny. Typ `range` je v podstatě ne-lze
    měnit (immutable) a generuje hodnoty v reálném čase, nikoliv všechny najednou.

    Syntaxe:
        - range(start, stop)  # Tvorba sekvence čísel
        - range(stop)         # Sekvence od 0 do stop
        - range(start, stop, step)  # Sekvence s daným krokem

    Příklady použití:
        - range(5)     # Vytváří range od 0 do 4
        - range(1, 10) # Vytváří range od 1 do 9
        - range(0, 10, 2) # Vytváří range s krokem 2: 0, 2, 4, 6, 8

    Validační proces:
        1. Ověřuje, zda hodnota je přesně instance typu range
        2. Kontroluje, že hodnota odpovídá typu `range`, což znamená, že se
           jedná o sekvenci čísel s definovaným začátkem, koncem a volitelným krokem

    Použití v kódu:
        - Pro parametry funkcí: def generate_numbers(r: range) -> List[int]
        - Pro generování číselných sekvencí: for i in range(10): ...
        - Pro typování proměnných: r: range = range(0, 5)

    Specifické použití:
        - Pro efektivní vytváření sekvencí čísel bez nutnosti uchovávat všechny hodnoty v paměti
        - Pro iterace s předdefinovanými rozsahy čísel
        - Pro generování hodnot, které budou použity v dalších výpočtech nebo operacích

    Kompatibilita:
        - `range` je kompatibilní s iterací (např. v `for` smyčkách)
        - `range` není kompatibilní s jinými typy sekvencí, jako jsou seznamy nebo n-tice
        - `range` není kompatibilní s operacemi, které modifikují hodnoty (např. přidávání, odebírání)

    Běžné chyby:
        - Zaměňování `range` s jinými sekvencemi, jako je seznam nebo n-tice
        - Použití `range` s nečíselnými hodnotami pro `start`, `stop` nebo `step`
        - Předpokládání, že `range` obsahuje všechny hodnoty najednou (ve skutečnosti je to generátor)
        - Nezohlednění, že `range` je uzavřený v horní mezí (tj. `range(1, 10)` neobsahuje hodnotu 10)

    Reference:
        - https://docs.python.org/3/library/functions.html#range
        - https://realpython.com/python-range/#how-to-use-the-range-function-in-python
    """

    VALIDATOR_KEY = "range"
    ANNOTATION = range

    IS_INSTANCE = range
    HAS_ATTRS = "__getitem__", "__len__", "__iter__", "start", "stop", "step"
    CALLABLE_ATTRS = "start", "stop", "step"

    DESCRIPTION = "Sekvence čísel v rozsahu"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je typu range, tedy neměnná sekvence čísel. "
            "Efektivně reprezentuje posloupnost čísel bez nutnosti jejich uložení v paměti."
        )
