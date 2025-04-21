from .valide_native_type import ValidateNativeType
from .validator_registry import TypeValidatorRegistry
from .vaidate_typing import ValidateTyping

class TypingPlus:

    # Metoda pro validaci typu
    validate_native_type = ValidateNativeType()

    # Metoda pro validaci typing anotace
    validate_typing = ValidateTyping()

    # Slovník s přístupem k validacím pro knihovnu tying
    registry = TypeValidatorRegistry()
