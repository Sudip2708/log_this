from typing import get_args, Union, Any

from ._base_type_validator import TypeValidator

class UnionValidator(TypeValidator):

    VALIDATOR_TYPE = Union  # není potřeba přímo, ale může být použito v registru

    def validate(self, value, annotation, inner_check=True):
        # Získání všech typů v rámci Unionu
        union_args = get_args(annotation)

        # Optat se zda je potřeba protože bez argumentů by to asi byla chyba?
        if not union_args:
            raise TypeError("Union bez parametrů není validní anotace.")

        for possible_type in union_args:
            try:
                inner_check_value = self.value_validator.get_new_inner_check(inner_check)
                if self.value_validator.validate(value, possible_type, inner_check_value):
                    return True
            except Exception:
                continue  # Ignorujeme výjimky, zkusíme další typ

        return False  # Ani jeden typ neprošel
