from typing import Any, Type, Union, get_origin, get_args


class TypeValidator:

    VALIDATOR_TYPE = None

    def __init__(self, value_validator):
        self.value_validator = value_validator

    def validate(self, value, annotation, inner_check=True):
        raise NotImplementedError("Musí být implementováno v podtřídě")


class ListValidator(TypeValidator):

    VALIDATOR_TYPE = list

    def validate(self, value, annotation, inner_check=True):
        if not isinstance(value, list):
            raise TypeError(f"Očekáván list, ale dostal jsem {type(value)}")

        if not inner_check:
            return True

        # Načtení vnitřních anotací
        # List může obsahovat pouze jednu, ale get_args vrací tuple, takže první položka [0] je hodnota kterou hledáme
        # Any je zde pro případ, kdyby byl obsah prázdný (pro starčí verze knihovny typing)
        inner_type = get_args(annotation)[0] if get_args(annotation) else Any

        for item in value:
            inner_check_value = self.value_validator.get_new_inner_check(inner_check)
            if not self.value_validator.validate(item, inner_type, inner_check_value):
                return False

        return True