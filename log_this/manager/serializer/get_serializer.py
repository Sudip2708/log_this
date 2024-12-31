from ._serializer_base import SafeSerializer


def get_serializer():
    """
    Hlavní funkce pro získání singleton instance pro serializaci.

    Returns:
        SafeSerializer: Instance pro serializaci.
    """
    return SafeSerializer()


