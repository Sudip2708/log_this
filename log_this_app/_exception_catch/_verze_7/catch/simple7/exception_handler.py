# exception_handler.py
"""Hlavní modul pro zpracování výjimek."""

from abc_helper import AbcSingletonMeta
import logging
import traceback
import functools
from typing import Dict, List, Optional, Type, Union, Callable, Any, Set, \
    get_type_hints

from exception_params import ExceptionHandlerParams
from handle_exception_base import HandleException


class ExceptionHandler(HandleException, metaclass=AbcSingletonMeta):
    """Hlavní třída pro zpracování výjimek."""

    def __init__(self, **kwargs):
        """Inicializuje singleton instanci ExceptionHandler."""
        # Kontrola, zda je již instance inicializována (singleton)
        if not hasattr(self, "_initialized"):
            # Inicializace rodiče
            super().__init__(**kwargs)

            # Atribut pro globální nastavení pro jednotlivé výjimky
            self._exception_handlers = {}

            # Potvrzení o singleton inicializaci
            self._initialized = True

    def define_exc_handler(self, exception: Type[Exception], **kwargs):
        """Vytvoří novou instanci HandleException na základě aktuálního nastavení.

        Args:
            exception: Typ výjimky, pro kterou se má vytvořit handler
            **kwargs: Další parametry, které přepíšou výchozí hodnoty

        Returns:
            HandleException: Nová instance HandleException
        """
        # Vytvoříme slovník všech výchozích hodnot z aktuální instance
        params = {}
        for param_name in ExceptionHandlerParams.get_param_info().keys():
            params[param_name] = getattr(self, param_name)

        # Přepíšeme výchozí hodnoty zadanými parametry
        params.update(kwargs)
        params[
            "exception"] = exception  # Zajistíme, že exception je vždy použita z argumentů

        # Vytvoříme novou instanci
        return HandleException(**params)

    def set_exception_handler(self, *exc_handlers: HandleException):
        """Přidá globální nastavení pro konkrétní výjimky do slovníku.

        Args:
            *exc_handlers: Instance HandleException pro přidání do globálního nastavení

        Raises:
            TypeError: Pokud některý z argumentů není instancí HandleException
            ValueError: Pokud již existuje handler se stejným klíčem
        """
        # Cyklus procházející jednotlivé položky
        for exc_handler in exc_handlers:
            # Kontrola vstupní hodnoty
            if not isinstance(exc_handler, HandleException):
                raise TypeError("Nebyla předaná instance HandleException.")

            # Načtení klíče
            key = str(exc_handler)

            # Kontrola, zda slovník již obsahuje klíč
            if key in self._exception_handlers:
                raise ValueError(
                    f"Přidávaný klíč {key} již ve slovníku existuje.")

            # Přidání klíče do slovníku
            self._exception_handlers[key] = exc_handler

        return self  # Pro řetězení volání

    def get_handler_for_exception(self,
                                  exception: Exception) -> HandleException:
        """Vrátí handler pro danou výjimku nebo výchozí handler.

        Args:
            exception: Instance výjimky

        Returns:
            HandleException: Handler pro danou výjimku nebo výchozí handler
        """
        # Hledáme handler pro danou výjimku
        exc_type = type(exception)
        key = f"_{exc_type.__name__}"

        return self._exception_handlers.get(key, self)

    def exception_catch(self, *exc_handlers: HandleException):
        """Dekorátor pro zachytávání specifikovaných výjimek a logování chyb.

        Args:
            *exc_handlers: Instance HandleException pro zachytávání výjimek

        Returns:
            Callable: Dekorátor pro zachytávání výjimek
        """
        # Převod HandleException instancí do slovníku pro rychlý přístup
        handlers = {}
        for handler in exc_handlers:
            if not isinstance(handler, HandleException):
                raise TypeError(f"{handler} není instance HandleException.")
            handlers[handler.exception] = handler

        # Definice dekorátoru
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # Najdeme správný handler pro výjimku
                    handler = None
                    for exc_type, exc_handler in handlers.items():
                        if isinstance(e, exc_type):
                            handler = exc_handler
                            break

                    # Pokud není nalezen specifický handler, použijeme výchozí
                    if handler is None:
                        handler = self.get_handler_for_exception(e)

                    # Zpracování výjimky
                    self.handle_exception(e, handler, func)

                    # Pokud je nastaveno raise_exception, znovu vyvoláme výjimku
                    if handler.raise_exception:
                        raise

            return wrapper

        return decorator

    def handle_exception(self, exception: Exception, handler: HandleException,
                         func: Callable):
        """Zpracuje výjimku podle daného handleru.

        Args:
            exception: Instance výjimky
            handler: Handler pro zpracování výjimky
            func: Funkce, ve které došlo k výjimce
        """
        # Sestavení zprávy pro log
        message = f"{handler.prefix} {handler.message} v {func.__name__}: {str(exception)}"

        # Logování
        logger = logging.getLogger()
        logger.log(handler.log_level, message)

        # Logování traceback, pokud je nastaveno
        if handler.include_traceback:
            tb_message = "".join(traceback.format_exc())
            logger.log(handler.log_level, tb_message)

        # Přidání prázdného řádku, pokud je nastaveno
        if handler.blank_line:
            logger.log(handler.log_level, "")

        # Spuštění akcí
        for action in handler.actions:
            try:
                action(exception)
            except Exception as action_exc:
                logger.error(f"Chyba při spouštění akce: {str(action_exc)}")


# Vytvoření globální instance
global_handler = ExceptionHandler()


# Export veřejných funkcí a tříd
def define_exc_handler(exception: Type[Exception], **kwargs):
    """Pomocná funkce pro vytvoření handleru výjimky."""
    return global_handler.define_exc_handler(exception, **kwargs)


def exc_catch(*exc_handlers: HandleException):
    """Dekorátor pro zachytávání výjimek."""
    return global_handler.exception_catch(*exc_handlers)