from typing import get_type_hints, Type, TypedDict, Dict

from ._dict_alike_base import DictAlikeBase


class TypedDictValidator(DictAlikeBase):
    """
    Validátor pro zápis TypedDict

    Hint:
        class Movie(TypedDict):
            name: str
            year: int

        MyDict = TypedDict('MyDict', {'field1': int, 'field2': str})
    """

    VALIDATOR_KEY = "typed_dict"
    ANNOTATION = TypedDict
    INFO = "Definuje strukturovaný slovník, kde každý klíč má pevně daný typ hodnoty."
    GET_ORIGIN = dict  # runtime je TypedDict instancí dict

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama (origin)
        self.validate_native_type(value, dict)

        # Kontrola zda je požadavek i na vnitřní validaci
        if not depth_check:
            return True

        # Získání informací o TypedDict
        # type_hints = getattr(annotation, "__annotations__", {})
        type_hints = get_type_hints(annotation)

        # Pokud nemáme žádné anotace, vrátíme True
        if not type_hints:
            return True

        # Získání informací o totalitě (total=True/False)
        # Total=True znamená, že všechny klíče jsou povinné
        # Total=False znamená, že klíče jsou volitelné
        is_total = getattr(annotation, "__total__", True)

        # Kontrola povinných klíčů
        if is_total:
            missing_keys = set(type_hints.keys()) - set(value.keys())
            if missing_keys:
                if bool_only:
                    return False
                raise KeyError(f"Chybí povinné klíče: {missing_keys}")

        # Vytvoření proměné pro zanoření
        depth = depth_check

        # Kontrola typů u existujících klíčů
        for key, val in value.items():

            # Odpočet zanoření pro další kontrolu
            depth = self._reduce_depth_check(depth)

            # Kontrola zanoření
            if not depth:
                break

            # Kontrola zda je klíč v type_hints
            self.validate_condition(key in type_hints, bool_only)

            # Kontrola na očekávaný typ
            expected_type = type_hints[key]
            self.validate_typing(
                val, expected_type, depth, custom_types, bool_only
            )

        return True