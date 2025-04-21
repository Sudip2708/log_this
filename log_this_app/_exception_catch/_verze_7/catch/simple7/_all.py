# exception_params.py
"""Modul definující parametry pro zpracování výjimek."""

import logging
from dataclasses import dataclass, field
from typing import Dict, List, Type, Union, Callable, Any, Set, Optional, \
    TypeVar, Generic

T = TypeVar('T')  # Proměnná typu pro generické typování


@dataclass
class ExceptionHandlerParams:
    """Definice parametrů pro zpracování výjimek."""
    # Definice typů a výchozích hodnot parametrů
    EXCEPTION_TYPE: Type[Type[Exception]] = Type[Exception]
    EXCEPTION_DEFAULT: Type[Exception] = Exception

    PREFIX_TYPE: Type[str] = str
    PREFIX_DEFAULT: str = "[CATCH]"

    MESSAGE_TYPE: Type[str] = str
    MESSAGE_DEFAULT: str = "Chyba při vykonávání"

    LOG_LEVEL_TYPE: Type[Union[int, str]] = Union[int, str]
    LOG_LEVEL_DEFAULT: Union[int, str] = logging.ERROR

    INCLUDE_TRACEBACK_TYPE: Type[bool] = bool
    INCLUDE_TRACEBACK_DEFAULT: bool = True

    BLANK_LINE_TYPE: Type[bool] = bool
    BLANK_LINE_DEFAULT: bool = True

    RAISE_EXCEPTION_TYPE: Type[bool] = bool
    RAISE_EXCEPTION_DEFAULT: bool = True

    ACTIONS_TYPE: Type[List[Callable]] = List[Callable]
    ACTIONS_DEFAULT: List[Callable] = field(default_factory=list)

    @classmethod
    def get_param_info(cls) -> Dict[str, Dict[str, Any]]:
        """Vrátí slovník s informacemi o všech parametrech."""
        params = {}
        # Vytvoříme slovník všech parametrů s jejich typy a výchozími hodnotami
        for param_name in dir(cls):
            if param_name.endswith("_TYPE"):
                # Extrahujeme základní název parametru (bez _TYPE)
                base_name = param_name[:-5].lower()
                # Získáme výchozí hodnotu z atributu _DEFAULT
                default_value_name = f"{param_name[:-5]}_DEFAULT"

                params[base_name] = {
                    "type": getattr(cls, param_name),
                    "default": getattr(cls, default_value_name, None),
                    "doc": f"Parametr {base_name} pro zpracování výjimky."
                }
        return params


# handle_exception_base.py
"""Základní modul pro zpracování výjimek."""

import inspect
from functools import wraps
from typing import Dict, List, Optional, Type, Union, Callable, Any, Set, \
    get_type_hints

from exception_params import ExceptionHandlerParams


def verify(value, expected_type):
    """Jednoduchá funkce pro ověření typu hodnoty."""
    if not isinstance(value, expected_type) and not (
            hasattr(expected_type, "__origin__") and
            isinstance(value, expected_type.__origin__)):
        raise TypeError(f"Očekáván typ {expected_type}, obdržen {type(value)}")
    return True


class ParameterDescriptor:
    """Deskriptor pro parametry třídy HandleException.

    Automatizuje gettery, settery a verifikaci pro atributy.
    """

    def __init__(self, name: str, param_type: Any, doc: str = None):
        self.name = name
        self.private_name = f"_{name}"
        self.param_type = param_type
        self.doc = doc

    def __get__(self, instance, owner):
        """Getter pro atribut."""
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        """Setter pro atribut s verifikací typu."""
        if value is not None:  # Povolíme None hodnoty
            verify(value, self.param_type)
        setattr(instance, self.private_name, value)


class HandleException:
    """Datová třída pro nastavení zpracování konkrétního typu výjimky."""

    # Dynamické vytvoření deskriptorů pro všechny parametry
    for param_name, param_info in ExceptionHandlerParams.get_param_info().items():
        locals()[param_name] = ParameterDescriptor(
            param_name,
            param_info["type"],
            param_info["doc"]
        )

    def __init__(self, **kwargs):
        """Inicializuje instanci s výchozími hodnotami a aktualizuje je podle zadaných argumentů."""
        # Nastavení výchozích hodnot
        for param_name, param_info in ExceptionHandlerParams.get_param_info().items():
            setattr(self, f"_{param_name}", param_info["default"])

        # Aktualizace hodnot podle zadaných argumentů
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"Neznámý atribut: {key}")

    def __str__(self):
        """Vrací textovou reprezentaci instance třídy pro uživatele."""
        return f"_{self.exception.__name__}"

    def set(self, **kwargs):
        """Nastaví více atributů najednou a vrátí instanci (pro řetězení volání)."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"Neznámý atribut: {key}")
        return self

    # Dynamické vytvoření set_* metod
    for param_name, param_info in ExceptionHandlerParams.get_param_info().items():
        method_name = f"set_{param_name}"

        def create_setter(name):
            """Tovární funkce pro vytvoření setteru."""

            def setter(self, value=None, accept_none=False):
                """Nastaví atribut a vrátí instanci (pro řetězení volání)."""
                if value is not None:
                    setattr(self, name, value)
                    return self
                if not accept_none:
                    raise ValueError(f"Nebyl předán parametr {name}")
                return self

            return setter

        # Nastavení správného názvu a dokumentace
        setter_method = create_setter(param_name)
        setter_method.__name__ = method_name
        setter_method.__doc__ = f"Nastaví parametr {param_name}."

        locals()[method_name] = setter_method

    def add_action(self, action: Callable, accept_none=False):
        """Přidá akci, která se má provést při zpracování výjimky."""
        if action is not None:
            verify(action, Callable)
            if callable(action):
                self.actions.append(action)
            else:
                raise TypeError("Akce musí být volatelná funkce nebo metoda.")
            return self
        if not accept_none:
            raise ValueError("Nebyl předán parametr action")
        return self


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


# Ukázka použití
if __name__ == "__main__":
    # Konfigurace logování
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    # Změna globálního nastavení
    global_handler.set_prefix("[GLOBAL]").set_message(
        "Chyba v globálním kontextu")

    # Definice handleru pro ValueError
    _ValueError = define_exc_handler(ValueError, message="Neplatná hodnota")

    # Registrace handleru v globálním nastavení
    global_handler.set_exception_handler(_ValueError)


    # Použití dekorátoru
    @exc_catch(_ValueError)
    def example_function(value):
        if not isinstance(value, int):
            raise ValueError("Hodnota musí být celé číslo")
        return value * 2


    # Test
    try:
        result = example_function("test")
    except ValueError:
        print("Výjimka byla znovu vyvolána, jak bylo nastaveno")