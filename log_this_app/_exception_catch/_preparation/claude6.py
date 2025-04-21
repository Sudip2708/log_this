import functools
import logging
from typing import Any, Callable, Optional, Type, Union, List, Tuple


class RetryableException(Exception):
    """Výjimka indikující možnost opakování."""
    pass


class ExceptionHandler:
    def __init__(self, *args, **kwargs):
        # Rozšíření konstruktoru o nové atributy
        self._default_handler = None
        self._global_handlers = {}
        self._exception_groups = {}
        self._retry_strategies = {}

    def set_default_handler(
            self,
            handler: Optional[Callable[[Exception], Any]] = None
    ) -> 'ExceptionHandler':
        """
        Nastavení globálního fallback handleru pro nezachycené výjimky.

        :param handler: Callable handler pro zpracování výjimek
        :return: Instance ExceptionHandleru
        """
        self._default_handler = handler
        return self

    def register_global_handler(
            self,
            handler: Callable[[Exception], Any],
            *exception_types: Type[Exception]
    ) -> 'ExceptionHandler':
        """
        Registrace globálního handleru pro specifické typy výjimek.

        :param handler: Callable handler pro zpracování výjimek
        :param exception_types: Typy výjimek k zachycení
        :return: Instance ExceptionHandleru
        """
        for exc_type in exception_types:
            self._global_handlers[exc_type] = handler
        return self

    def create_exception_group(
            self,
            group_name: str,
            *exception_types: Type[Exception]
    ) -> 'ExceptionHandler':
        """
        Vytvoření skupiny příbuzných výjimek.

        :param group_name: Název skupiny výjimek
        :param exception_types: Typy výjimek ve skupině
        :return: Instance ExceptionHandleru
        """
        self._exception_groups[group_name] = list(exception_types)
        return self

    def set_retry_strategy(
            self,
            exception_type: Type[Exception],
            max_attempts: int = 3,
            delay: float = 1.0,
            backoff_factor: float = 2.0,
            retriable_exceptions: Tuple[Type[Exception], ...] = (
            RetryableException,)
    ) -> 'ExceptionHandler':
        """
        Nastavení strategie opakování pro specifické výjimky.

        :param exception_type: Typ výjimky pro strategii opakování
        :param max_attempts: Maximální počet opakování
        :param delay: Počáteční prodleva mezi pokusy
        :param backoff_factor: Faktor pro exponenciální nárůst prodlevy
        :param retriable_exceptions: Typy výjimek, které umožňují opakování
        :return: Instance ExceptionHandleru
        """
        self._retry_strategies[exception_type] = {
            'max_attempts': max_attempts,
            'delay': delay,
            'backoff_factor': backoff_factor,
            'retriable_exceptions': retriable_exceptions
        }
        return self

    def catch(self, *args, **kwargs):
        """
        Rozšíření původní metody catch o nové funkcionality.
        Zde by byla implementována logika pro:
        - Globální handlery
        - Skupiny výjimek
        - Strategie opakování
        """

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*func_args, **func_kwargs):
                # Logika opakování a zpracování výjimek
                attempts = 0
                while True:
                    try:
                        return func(*func_args, **func_kwargs)
                    except Exception as e:
                        # Globální handlery
                        for exc_type, handler in self._global_handlers.items():
                            if isinstance(e, exc_type):
                                return handler(e)

                        # Default handler
                        if self._default_handler:
                            return self._default_handler(e)

                        # Strategie opakování
                        retry_config = self._retry_strategies.get(type(e))
                        if retry_config:
                            attempts += 1
                            if attempts < retry_config['max_attempts']:
                                # Exponenciální backoff
                                import time
                                time.sleep(
                                    retry_config['delay'] *
                                    (retry_config['backoff_factor'] ** attempts)
                                )
                                continue

                        # Pokud žádná strategie nezabrala, vyvolej výjimku
                        raise

            return wrapper

        return decorator


# Příklad použití
def example_usage():
    handler = ExceptionHandler()

    # Nastavení globálního handleru
    handler.register_global_handler(
        lambda e: print(f"Zachycena globální výjimka: {e}"),
        ValueError, TypeError
    )

    # Nastavení default handleru
    handler.set_default_handler(
        lambda e: print(f"Nezachycená výjimka: {e}")
    )

    # Vytvoření skupiny výjimek
    handler.create_exception_group(
        "data_errors",
        ValueError, TypeError, KeyError
    )

    # Nastavení strategie opakování
    handler.set_retry_strategy(
        ValueError,
        max_attempts=3,
        delay=0.5
    )

    @handler.catch()
    def example_function(x, y):
        return x / y