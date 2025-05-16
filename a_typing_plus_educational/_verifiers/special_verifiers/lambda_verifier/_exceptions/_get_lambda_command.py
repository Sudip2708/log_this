from typing import Any, Callable
import inspect


def _get_lambda_repr(lambda_command: Callable[[Any], bool]):
    """
    Pomocná funkce pro získání reporezentace objektu lambda příkazu

    Používá omezení na 100 znaků pro případ dlouhého zápisu.
    """

    repr_lambda = repr(lambda_command)
    return (
        repr_lambda
        if len(repr_lambda)<100
        else repr_lambda[99] + "..."
    )


def get_lambda_command(lambda_command: Callable[[Any], bool]):
    """
    Pomocná funkce pro získání lambda příkazu

    Funkce buď vrátí print lambda příkazu, jeli dostupný,
    nebo oznam o tom, že lambda příkaz nelze načíst,
    s popisem chyb a reprezentací objektu.

    """

    try:
        return inspect.getsource(lambda_command).strip()

    except Exception as e:
        return f"<Příkaz nelze načíst. Zachycená výjimka: {e} Objekt: {repr(lambda_command)}>"
