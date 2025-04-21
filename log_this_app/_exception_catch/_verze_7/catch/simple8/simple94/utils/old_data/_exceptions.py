# Výjimka pro chyby ověření
class InvalidPathInputError(TypeError):
    """Výjimka vyvolaná při nesprávném typu vstupu pro cestu."""


# Výjimka pro neočekávané chyby
class VerifyUnexpectedError(Exception):
    """Výjimka vyvolaná při neočekávané události."""