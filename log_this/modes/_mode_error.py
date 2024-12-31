from typing import Any, Callable
import logging
import inspect


def mode_error(
    logger: logging.Logger,
    func: Callable[..., Any],
    args: tuple,
    kwargs: dict,
    serialize: Callable[..., Any],
    indent: str = "",
    start_blank: str = "",
    end_blank: str = ""
) -> Any:
    """
    Loguje chybu při použití dekorátoru @log_this, pokud není definován platný režim,
    a následně spustí původní funkci.

    Args:
        logger (logging.Logger): Logger pro logování zpráv.
        func (Callable): Funkce, která byla dekorována a u které došlo k chybě.
        args (tuple): Argumenty předané dekorované funkci.
        kwargs (dict): Klíčové argumenty předané dekorované funkci.
        serialize (Callable): Metoda pro serializaci hodnot.
        indent (str, optional): Řetězec pro odsazení logovací zprávy. Default je "".
        start_blank (str, optional): Řetězec přidaný na začátek zprávy pro prázdný řádek. Default je "".
        end_blank (str, optional): Řetězec přidaný na konec zprávy pro prázdný řádek. Default je "".

    Returns:
        Any: Výsledek volání původní dekorované funkce s předanými argumenty.

    Notes:
        Funkce loguje chybu s detaily o názvu funkce a její lokaci v souboru.
    """

    # Logování chyby
    logger.error(
        f"{start_blank}{indent}# LogThis ERROR:"
        f"\n{indent}# >>> A valid mode for the @log_this decorator is not defined"
        f"\n{indent}# >>> Function: {func.__name__}{tuple(serialize(args))}"
        f"\n{indent}# >>> File: {inspect.getfile(func)}{end_blank}"
    )

    # Volání původní funkce s argumenty
    return func(*args, **kwargs)
