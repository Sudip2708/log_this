from typing import Any, get_origin, Union, Tuple, Literal, Optional


TypingType = Any

class TypingValidator:

    # Metoda pro validaci typu
    validate_native_type = ValidateNativeType()

    # Metoda pro validaci podmínky
    validate_condition = ValidateCondition()

    # Slovník s přístupem k validacím pro knihovnu tying
    registry = TypeValidatorRegistry()

    def __call__(
            self,
            value: Any,
            annotation: Optional[type, TypingType, Tuple[Union[type, TypingType], ...]] = None,
            depth_check: Union[Literal["all"], int] = "all",  # Nastavení hloubky kontroly vnitřních typů
            custom_types: Optional[Tuple[Any, ...]] = None,  # Specifikace vlastních typů, a tříd, předaných jako tuple pro kontrolu vzorů
            bool_only: bool = False  # Specifkace zda vyvysovat neshody jako výjimky a nebo jen vracet false
    ):

        # Pokud není zadaná hodnota a podmínka a je tedy zadaná pouze podmnka (jako hodnota)
        if not annotation:
            return self.validate_condition(value)

        # Jednoduché typy str, int, ...
        # Po této kotrole je jasné, že nebyl zadaný pouze nativní typ
        if isinstance(annotation, type):
            return self.validate_native_type(value, annotation)

        # Načtení validátoru pro ovalidované typy z knihovny typing
        # Tato kontrola odhalí ty anotace, které mají origin a k nim definovanou validaci
        # origin = get_origin(annotation)
        validator = self.registry.get_annotation_validator(annotation)
        if validator:
            return validator(value, annotation, depth_check, custom_types, bool_only)

        # Vlastní typy v custom_types
        if custom_types:
            for custom_type in custom_types:
                if isinstance(annotation, custom_type):
                    return custom_type.validate(value)

        # Nikde nenalezeno → chyba
        raise TypeError(f"Unsupported type annotation: {annotation}")


validate_typing = ValidateTyping()