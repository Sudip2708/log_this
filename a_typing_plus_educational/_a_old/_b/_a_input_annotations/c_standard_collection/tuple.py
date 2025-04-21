from typing import get_args, Tuple

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T, T1, T2, T3


class TupleValidator(BaseIterableValidator):
    """
    Validátor pro zápis Tuple[T1, T2, ...] a Tuple[T, ...]

    Hint:
        Tuple[T1, T2, T3] = N-tice s přesnými typy na daných pozicích
        Tuple[T, ...] = N-tice s libovolným počtem položek stejného typu
    """

    VALIDATOR_KEY = "tuple"
    ANNOTATION = Tuple[T1, T2, T3], Tuple[T, ...]
    INFO = "Definuje n-tici"
    GET_ORIGIN = tuple

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama (origin)
        self.validate_native_type(value, self.GET_ORIGIN)

        # Kontrola zda je požadavek i na vnitřní validaci
        if not depth_check:
            return True

        # Načtení vnitřních anotací
        inner_args = get_args(annotation)

        # Pokud nemáme specifikované vnitřní typy, vrátíme True
        if not inner_args:
            return True

        # Zjištění, zda se jedná o variabilní n-tici (Tuple[T, ...])
        is_variable_tuple = len(inner_args) == 2 and inner_args[1] == Ellipsis

        # Variabilní n-tice (Tuple[T, ...])
        if is_variable_tuple:

            # Načtení typu
            item_type = inner_args[0]

            # Vytvoření vlastní hloubky
            depth = depth_check

            # Kontrola všech položek proti stejnému typu
            for item in value:

                # Změna hloubky
                depth = self._reduce_depth_check(depth)

                # Validace hodnoty
                self.validate_typing(
                    item, item_type, depth, custom_types, bool_only
                )

                # Kontrola vyčerpání zanoření (přerušení cyklu)
                if not depth_check:
                    break

        # Fixní n-tice (Tuple[T1, T2, ...])
        else:

            # Kontrola délky
            if len(value) != len(inner_args):
                raise ValueError(
                    f"Očekávaná délka n-tice {len(inner_args)}, ale obdrženo {len(value)}")

            # Vytvoření vlastní hloubky
            depth = depth_check

            # Kontrola typu každé položky na dané pozici
            for i, (item, item_type) in enumerate(zip(value, inner_args)):

                # Změna hloubky
                depth = self._reduce_depth_check(depth)

                # Validace hodnoty
                self.validate_typing(
                    item, item_type, depth, custom_types, bool_only
                )

                # Kontrola vyčerpání zanoření (přerušení cyklu)
                if not depth_check:
                    break

        return True