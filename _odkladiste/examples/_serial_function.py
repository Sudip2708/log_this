from typing import List, Any
from log_this_old import log_this


@log_this(2)
def second_function_addition(first_number: int, second_number: int) -> int:
    """Druhá testovací funkce pro dekorátor @log_this() nabízející sečtení dvou int hodnot.

    Funkce nejprve ověří vstupní hodnoty, zda jsou typu int.
    Pokud ano sečte je a vrátí výsledek.
    Pokud ne vyvolá výjimku.

    Args:
        first_number (int): První číslo pro sečtení.
        second_number (int): Druhé číslo pro sečtení.

    Returns:
        int: Součet prvního a druhého čísla.

    Raises:
        ValueError: Pokud některý z vstupních parametrů není typu int.
    """

    if not isinstance(first_number, int):
        raise ValueError("První číslo není typu 'int'")
    if not isinstance(second_number, int):
        raise ValueError("Druhé číslo není typu 'int'")

    return first_number + second_number

@log_this(2)
def third_function_comparison(element, comparison_set):
    """Třetí testovací funkce pro dekorátor @log_this() nabízející porovnání prvku v sadě.

    Uvnitř bloku try/except dojde k porovnání, zda se element nachází v testovací sadě.
    Pokud bude nalezen vrátí se True, jinak False.

    Args:
        element: Prvek k porovnání.
        comparison_set: Sada hodnot pro porovnání.

    Returns:
        bool: True, pokud je prvek v sadě, jinak False.

    Raises:
        TypeError: Pokud comparison_set není iterovatelný nebo typ elementu není kompatibilní.
        ValueError: Pokud interní metoda vyžaduje konkrétní hodnoty.
        RuntimeError: Pokud byl během iterace modifikován iterovatelný objekt.
    """

    try:
        return element in comparison_set
    except TypeError as e:
        raise TypeError(f"TypeErrorHint: "
                        f"comparison_set není iterovatelný "
                        f"nebo typ element není kompatibilní "
                        f"s typy v comparison_set: {e}")
    except ValueError as e:
        raise ValueError(f"ValueErrorHint: "
                         f"interní metoda vyžaduje konkrétní hodnoty "
                         f"a při nesprávné hodnotě selže: {e}")
    except RuntimeError as e:
        raise RuntimeError(f"RuntimeErrorHint: "
                           f"během iterace modifikován iterovatelný objekt: "
                           f"{e}")


@log_this(2)
def first_function_nesting(
        first_number: int,
        second_number: int,
        comparison_set: List[Any]
) -> bool:
    """První testovací funkce pro dekorátor @log_this() nabízející vnořené volání dvou metod.

    Funkce nejprve zavolá funkci pro sečtení dvou čísel.
    Následně volá funkci pro ověření, zda je výsledná hodnota obsažena v přidaném seznamu hodnot.

    Args:
        first_number (int): První číslo pro sečtení.
        second_number (int): Druhé číslo pro sečtení.
        comparison_set (List[Any]): Seznam hodnot pro ověření.

    Returns:
        bool: Výsledek porovnání sečtené hodnoty v sadě hodnot.
    """

    result = second_function_addition(first_number, second_number)
    return third_function_comparison(result, comparison_set)


# Spuštění ukázky
if __name__ == "__main__":
    a = second_function_addition(3,4)
    b = third_function_comparison(a, list(range(5,10)))
    c = first_function_nesting(3, 4, list(range(5,10)))



