from typing import Callable, Any
from datetime import datetime

from .utils import (
    safe_serialize,
    loger_settings
)


def log_simple(
    func: Callable,
    args: tuple,
    kwargs: dict,
    indent: str = "",
    start_blank: str = "",
    end_blank: str = ""
) -> Any:
    """
    Loguje informace o volání funkce v režimu 'simple', včetně vstupních parametrů,
    výsledku a případných výjimek.

    Args:
        func (Callable): Funkce, jejíž volání je logováno.
        args (tuple): Argumenty předané logované funkci.
        kwargs (dict): Klíčové argumenty předané logované funkci.
        indent (str, optional): Řetězec pro odsazení logovací zprávy. Default je "".
        start_blank (str, optional): Řetězec přidaný na začátek zprávy pro prázdný řádek. Default je "".
        end_blank (str, optional): Řetězec přidaný na konec zprávy pro prázdný řádek. Default je "".

    Returns:
        Any: Výsledek volání původní dekorované funkce s předanými argumenty.

    Notes:
        Funkce loguje detailní informace o průběhu volání, včetně času spuštění,
        vstupních parametrů, výstupu a případně zachycených výjimek. Nakonec
        loguje ukončení běhu funkce.
    """


    # Inicializace logeru a začátek měření jeho běhu
    logger = loger_settings()

    # Úvodní zpráva
    logger.debug(f"{start_blank}{indent}"
                 f"# START LogThis('simple') "
                 f"↓ {datetime.now()} "
                 f"↓ {func.__name__} ↓")
    logger.debug(f"{indent}"
                 f"# >>> Input parameters: {safe_serialize(args)}")

    # Volání funkce
    try:
        result = func(*args, **kwargs)
        logger.debug(f"{indent}"
                     f"# >>> Outcome: {result}")
        return result

    # Zachycení výjimky
    except Exception as e:
        logger.debug(f"{indent}"
                     f"# >>> Outcome: Raised exception {type(e).__name__}"
                     f": {str(e)}")
        raise

    # Dodatek
    finally:
        logger.debug(f"{indent}"
                     f"# END LogThis('simple') "
                     f"↑ {func.__name__} "
                     f"↑ {end_blank}")


