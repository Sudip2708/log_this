from typing import Tuple

from .._base_type_validator import TypeValidator


class TupleValidator(TypeValidator):
    """
    Validátor pro zápis Tuple[T1, T2, ...] a Tuple[T, ...]

    Hint:
        Tuple[T1, T2, T3] = N-tice s přesnými typy na daných pozicích
        Tuple[T, ...] = N-tice s libovolným počtem položek stejného typu
    """

    # Definice klíče pro registr
    VALIDATOR_TYPE = Tuple

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama (origin)
        self.validate_native_type(value, tuple)

        # Kontrola zda je požadavek i na vnitřní validaci
        if not depth_check:
            return True

        # Načtení vnitřních anotací
        inner_args = self._get_inner_args(annotation)

        # Pokud nemáme specifikované vnitřní typy, vrátíme True
        if not inner_args:
            return True

        # Zjištění, zda se jedná o variabilní n-tici (Tuple[T, ...])
        is_variable_tuple = len(inner_args) == 2 and inner_args[1] == Ellipsis

        # Variabilní n-tice (Tuple[T, ...])
        if is_variable_tuple:
            item_type = inner_args[0]

            # Kontrola všech položek proti stejnému typu
            for item in value:
                new_depth_check = self._reduce_depth_check(depth_check)
                self.validate_typing(item, item_type, new_depth_check,
                                     custom_types, bool_only)

        # Fixní n-tice (Tuple[T1, T2, ...])
        else:
            # Kontrola délky
            if len(value) != len(inner_args):
                raise ValueError(
                    f"Očekávaná délka n-tice {len(inner_args)}, ale obdrženo {len(value)}")

            # Kontrola typu každé položky na dané pozici
            for i, (item, item_type) in enumerate(zip(value, inner_args)):
                new_depth_check = self._reduce_depth_check(depth_check)
                self.validate_typing(item, item_type, new_depth_check,
                                     custom_types, bool_only)

        return True