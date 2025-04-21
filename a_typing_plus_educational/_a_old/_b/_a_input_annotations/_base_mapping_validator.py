from typing import get_args

from ._base_type_validator import BaseTypeValidator


class BaseMappingValidator(BaseTypeValidator):
    """
    Základní třídy pro slovníkové anotace.


    Z této třídy dědí logyku následující třídy:
        DefaultDict[K, V] -  jako dict, ale s výchozí hodnotou
        OrderedDict[K, V] -  slovník s garantovaným pořadím
        Mapping[K, V] -  read-only dictionary interface
        MutableMapping[K, V] -  mutable interface
    """

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama (origin)
        self.validate_native_type(value, self.GET_ORIGIN)

        # Kontrola zda je požadavek i na vnitřní validaci
        if not depth_check:
            return True

        # Načtení vnitřních anotací pro klíče a hodnoty
        inner_args = get_args(annotation)

        # Pokud nemáme specifikované typy pro klíče a hodnoty, vrátíme True
        if not inner_args:
            return True

        # Načtení klíče a hodnoty
        key_type, value_type = inner_args

        # Cyklus pro kontrolu klíčů a hodnot
        for key, val in value.items():

            # Odpočet zanoření pro další kontrolu
            depth_check = self._reduce_depth_check(depth_check)

            # Validace klíče
            self.validate_typing(
                key, key_type, depth_check, custom_types, bool_only
            )

            # Validace hodnoty
            self.validate_typing(
                val, value_type, depth_check, custom_types, bool_only
            )

            # Kontrola vyčerpání zanoření (přerušení cyklu)
            if not depth_check:
                break

        return True

