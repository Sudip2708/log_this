from typing import TypeVar, get_origin, get_args, Ellipsis

from ._base import BaseValidator
from ...verify import verify

class ListValidator(BaseValidator):

    NAME = "tuple"
    TYPING = "Tuple[...]"
    TYPE = tuple

    @staticmethod
    def validate_items(value, expected_type, deep_check):
        inner_type = get_args(expected_type)
        repeater = inner_type[-1] == Ellipsis

        if not repeater:
            # Přesné ověření, bez opakování
            if len(value) != len(inner_type):
                return False  # Počet prvků neodpovídá
            for val, typ in zip(value, inner_type):
                if not verify(val, typ, deep_check):
                    return False
        else:
            # Ověření s opakováním
            types_to_repeat = inner_type[:-1]  # Typy pro opakování
            for i, val in enumerate(value):
                type_index = i % len(types_to_repeat)
                if not verify(val, types_to_repeat[type_index], deep_check):
                    return False

        return True

        # Zakomponovat do těchto kontol vyvolání výjmky s příslušným textem!
        # Zjistit co je lepší přístup, jestli to a nebo jen false, ale podle mě zde je místo pro přesné zacílení na danou chybu.




        # # Ověření pro Tuple[T, ...] (homogenní n-tice)
        # if not isinstance(args, tuple) and not isinstance(args, list):
        #     return all(
        #         verify(item, args, deep_check)
        #         for item in value
        #     )
        #
        # # Ověření pro Tuple[T1, T2, ...] (heterogenní n-tice)
        # return len(value) == len(args) and all(
        #     verify(value[i], args[i], deep_check)
        #     for i in range(len(args))
        # )


"""
Rozdíl mezi homogenním a heterogenním tuplem spočívá v tom, zda všechny prvky tuple mají stejný typ nebo různé typy.

Homogenní tuple:
Obsahuje prvky stejného typu.
Například Tuple[int, ...], což znamená tuple s libovolným počtem celých čísel.
V tomto případě get_args(expected_type) vrátí (int, Ellipsis). Ellipsis indikuje, že tuple může obsahovat libovolný počet prvků daného typu.
Heterogenní tuple:
Obsahuje prvky různých typů.
Například Tuple[str, int, float], což znamená tuple s přesně definovanými typy prvků.
V tomto případě get_args(expected_type) vrátí (str, int, float).
Tuple[str, int, ...] je také možné, a v tomto případě get_args(expected_type) vrátí (str, int, Ellipsis) a znamená, že tuple musí obsahovat alespoň jeden prvek typu string, a alespoň jeden prvek typu int, a pak může obsahovat libovolný počet dalších prvků.
Rozdíl ve výstupu get_args():

Pro homogenní tuple bude výstupem tuple s jedním typem a Ellipsis.
Pro heterogenní tuple bude výstupem tuple s konkrétními typy prvků.
Použití Ellipsis:

Ellipsis (symbol ...) se používá k označení, že tuple může mít libovolný počet prvků stejného typu.
"""
