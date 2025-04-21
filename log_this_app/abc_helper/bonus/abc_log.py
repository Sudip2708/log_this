import functools
import logging
from typing import Any, Callable


def abc_log(log_level: int = logging.DEBUG) -> Callable:
    """
    Dekorátor pro přidání logování abstraktním metodám.

    Výhody:
    - Automatické logování volání abstraktních metod
    - Konfigurovatelná úroveň logování
    - Sledování průběhu volání metod před jejich implementací

    Příklady použití:
    1. Ladění: Sledování volání ještě neimplementovaných metod
    2. Audit: Záznam pokusů o volání abstraktních metod
    3. Diagnostika: Identifikace míst, kde chybí implementace

    Args:
        log_level: Úroveň logování (výchozí DEBUG)

    Returns:
        Dekorovaná metoda s logovací logikou
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger = logging.getLogger(func.__module__)

            # Základní informace pro logging
            log_info = {
                'method': func.__name__,
                'class': args[0].__class__.__name__ if args else 'Unknown',
                'args': args[1:],
                'kwargs': kwargs
            }

            # Zalogování volání abstraktní metody
            logger.log(
                log_level,
                f"Abstract method called: {log_info['method']} "
                f"in {log_info['class']}"
            )

            # Volitelně můžeme přidat více detailů
            logger.debug(f"Method details: {log_info}")

            # Vyvolání původní abstraktní metody (která typicky vyhodí NotImplementedError)
            return func(*args, **kwargs)

        return wrapper

    return decorator


# # Příklad použití
# class ExampleAbstractClass(ABC):
#
#     @abc_log(logging.INFO)
#     @abstractmethod
#     def example_method(self, param1: str, param2: int) -> bool:
#         """Abstraktní metoda s logováním."""
#         pass