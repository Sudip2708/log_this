from typing import get_args, Tuple

from .._base_type_var import T, T1, T2, T3
from ._tuple_alike_base import TupleAlikeBase


class NamedTupleValidator(TupleAlikeBase):
    """
    Validátor pro zápis Tuple[T1, T2, ...] a Tuple[T, ...]

    Hint:
        Tuple[T1, T2, T3] = N-tice s přesnými typy na daných pozicích
        Tuple[T, ...] = N-tice s libovolným počtem položek stejného typu
    """

    VALIDATOR_KEY = "namedtuple"
    ANNOTATION = "NamedTuple"  # Symbolický zápis, není konkrétní typ jako Tuple[int, str]
    INFO = "Definuje n-tici s pojmenovanými položkami"
    GET_ORIGIN = tuple

    @staticmethod
    def is_named_tuple(annotation):
        """Metoda pro ověření, že se jedná o NamedTuple objekt"""
        return (
                isinstance(annotation, type)
                and issubclass(annotation, tuple)
                and hasattr(annotation, "__annotations__")
                and hasattr(annotation, "_fields")
        )

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama (origin)
        self.validate_native_type(value, self.GET_ORIGIN)

        # Pokud není požadavek na vnitřní kontrolu, vrátíme True
        if not depth_check:
            return True

        # Získání anotací
        field_types = getattr(annotation, "__annotations__", None)

        if not field_types:
            return True  # Nemáme definované typy, nemáme co kontrolovat

        for field_name, expected_type in field_types.items():

            # Získání hodnoty (dle jména)
            field_value = getattr(value, field_name)

            # Snížení hloubky
            depth_check = self._reduce_depth_check(depth_check)

            # Validace hodnoty v poli
            self.validate_typing(
                field_value, expected_type, depth_check, custom_types, bool_only
            )

            # Přerušení v případě vyčerpání hloubky
            if not depth_check:
                break

        return True