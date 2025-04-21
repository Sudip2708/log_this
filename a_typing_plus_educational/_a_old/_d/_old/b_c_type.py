from typing import Type as TypeAnnotation

from .._base_type_validator import TypeValidator


class TypeTypeValidator(TypeValidator):
    """
    Validátor pro zápis Type[T]

    Type reprezentuje třídu objektu, nikoli instanci.

    Hint:
        def process_class(cls: Type[BaseClass]) -> None:
            # cls je třída, která dědí z BaseClass, nikoli instance
            ...
    """

    # Definice klíče pro registr
    VALIDATOR_TYPE = TypeAnnotation

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Kontrola, zda je hodnota třída (nikoli instance)
        if not isinstance(value, type):
            if bool_only:
                return False
            raise TypeError(
                f"Očekávána třída (type), ale obdrženo {type(value).__name__}")

        # Kontrola zda je požadavek i na vnitřní validaci
        if not depth_check:
            return True

        # Načtení vnitřních anotací
        inner_args = self._get_inner_args(annotation)

        # Pokud není specifikován konkrétní typ, vrátíme True
        if inner_args is None or inner_args == ...:
            return True

        # Kontrola, zda je třída podtřídou specifikované třídy
        if not issubclass(value, inner_args):
            if bool_only:
                return False
            raise TypeError(
                f"Očekávána třída odvozená od {inner_args.__name__}, ale obdrženo {value.__name__}")

        return True