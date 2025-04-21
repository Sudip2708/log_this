from typing import Any, Type, Union, get_origin, get_args


class TypeValidatorRegistry:
    def __init__(self):
        self.validators = {}

    def register(self, origin_type, validator_class):
        self.validators[origin_type] = validator_class

    def get_validator(self, annotation):
        origin = get_origin(annotation)
        if origin in self.validators:
            return self.validators[origin]
        return None


class ValueValidator:

    def __init__(self):
        self.registry = TypeValidatorRegistry()
        # Registrace validátorů
        self.registry.register(list, ListValidator(self))


    def get_new_inner_check(self, inner_check):
        if isinstance(inner_check, int):
            return inner_check - 1 if inner_check > 0 else False
        return inner_check


    def validate(self, value, annotation, inner_check=True):
        # Jednoduché typy
        if isinstance(annotation, type):
            return isinstance(value, annotation)

        # Zpracování typů z typing modulu
        origin = get_origin(annotation)
        if origin is None:
            # Některé speciální případy jako Any, ...
            # Pořešit potom
            pass

        validator = self.registry.get_validator(origin)
        if validator:
            return validator.validate(value, annotation, inner_check)

        # Pokud nemáme validátor, pokusíme se o jednoduchou validaci
        if isinstance(origin, type):
            return isinstance(value, origin)

        # Neznámý typ
        raise TypeError(f"Nepodporovaný typ anotace: {annotation}")