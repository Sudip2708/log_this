from typing import Callable, Any
from datetime import datetime

from .utils import (
    safe_serialize,
)


def log_one_line(
    logger,
    func: Callable,
    args: tuple,
    kwargs: dict,
    indent: str = "",
    start_blank: str = "",
    end_blank: str = ""
) -> Any:
    """
    Loguje informace o volání funkce v jednorzádkovém formátu.

    Args:
        logger: Logger pro logování zpráv.
        func (Callable): Funkce, jejíž volání je logováno.
        args (tuple): Argumenty předané logované funkci.
        kwargs (dict): Klíčové argumenty předané logované funkci.
        indent (str, optional): Řetězec pro odsazení logovací zprávy. Default je "".
        start_blank (str, optional): Řetězec přidaný na začátek zprávy pro prázdný řádek. Default je "".
        end_blank (str, optional): Řetězec přidaný na konec zprávy pro prázdný řádek. Default je "".

    Returns:
        Any: Výsledek volání původní dekorované funkce s předanými argumenty.

    Notes:
        Funkce loguje volání funkce v jednorzádkovém formátu, včetně času, jména funkce
        a serializovaných hodnot argumentů.
    """

    # Logování jednorzádkové zprávy
    logger.info(
        f"{start_blank}{indent}"
        f"# INFO LogThis('one_line') "
        f"| {datetime.now()} "
        f"| {func.__name__}{tuple(safe_serialize(args))} "
        f"{end_blank}"
    )

    # Volání původní funkce s argumenty
    return func(*args, **kwargs)
