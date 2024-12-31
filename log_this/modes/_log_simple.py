from typing import Callable, Any
import logging
from datetime import datetime


def log_simple(
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
    Loguje informace o volání funkce v režimu 'simple', včetně vstupních parametrů,
    výsledku a případných výjimek.

    Args:
        logger (logging.Logger): Logger pro logování zpráv.
        func (Callable): Funkce, jejíž volání je logováno.
        args (tuple): Argumenty předané logované funkci.
        kwargs (dict): Klíčové argumenty předané logované funkci.
        serialize (Callable): Metoda pro serializaci hodnot.
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

    # Úvodní zpráva
    logger.debug(f"{start_blank}{indent}"
                 f"# START LogThis('simple') "
                 f"↓ {datetime.now()} "
                 f"↓ {func.__name__} ↓")
    logger.debug(f"{indent}"
                 f"# >>> Input parameters: {serialize(args)}")

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


