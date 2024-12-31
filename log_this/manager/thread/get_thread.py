from ._context import ThreadContext


def get_thread():
    """
    Hlavní funkce pro získání vlákna.
    """
    return ThreadContext()


