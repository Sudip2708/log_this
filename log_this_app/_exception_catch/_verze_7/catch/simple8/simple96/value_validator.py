from typing import Any, Type, Union, get_origin, get_args


from ._type_validator_registry import TypeValidatorRegistry

class ValueValidator:

    def __init__(self):
        # Načtení všech validačních sad
        self.registry = TypeValidatorRegistry(self)

    @staticmethod
    def get_new_inner_check(inner_check):
        if isinstance(inner_check, int):
            return inner_check - 1 if inner_check > 0 else False
        return inner_check


    def validate(
            self,
            value,
            annotation,
            inner_check=True,
            specification=None,  # Specifikace vlastních typů, a tříd, předaných jako tuple pro kontrolu vzorů
            bool_only = False  # Specifkace zda vyvysovat neshody jako výjimky a nebo jen vracet false
    ):

        # Jednoduché typy str, int, ...
        if isinstance(annotation, type):
            return isinstance(value, annotation)

        # Pokud je validace Any, vrací vždy True
        if annotation is Any:
            return True

        # Zpracování typů z typing modulu
        origin = get_origin(annotation)

        # Přednostní zpracování příkazů jako Union, či vlastních typových anotací
        if origin is None:
            # Některé speciální případy jako Any, ...
            # Pořešit potom
            pass

        # Načtení validátoru pro daný typ
        validator = self.registry.get_validator(origin)
        if not validator:
            raise TypeError(f"Nepodporovaný typ anotace: {annotation}")

        # Rekurzivní volání validace
        try:
            return validator.validate(value, annotation, inner_check)
        except Exception:
            # Neznámý typ
            raise