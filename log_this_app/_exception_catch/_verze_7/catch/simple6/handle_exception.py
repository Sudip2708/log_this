import logging
from typing import Dict, List, Optional, Type, Union, Callable, Any, Set

from verify import verify

class HandleException:
    """Datová třída pro nastavení zpracování konkrétního typu výjimky."""

    # Doplnit kontroly pro seter

    def __init__(
            self,
            exception: Type[Exception],
            prefix: str = "[CATCH]",
            message: str = "Chyba při vykonávání",
            log_level: Union[int, str] = logging.ERROR,
            include_traceback: bool = True,
            blank_line: bool = True,
            raise_exception: bool = True,
            actions: List[Callable] = None
    ):
        self.exception = exception
        self.prefix = prefix
        self.message = message
        self.log_level = log_level
        self.include_traceback = include_traceback
        self.blank_line = blank_line
        self.raise_exception = raise_exception
        self.actions = actions or []

    def __str__(self):
        """Vrací textovou reprezentaci instance třídy pro uživatele."""
        return f"_{self.exception.__name__}"

    def set(
            self,
            exception: Type[Exception] = None,
            prefix: str = None,
            message: str = None,
            log_level: Union[int, str] = None,
            include_traceback: bool = None,
            blank_line: bool = None,
            raise_exception: bool = None,
            actions: List[Callable] = None
    ):

        self.set_exception(exception, accept_none=True)
        self.set_prefix(prefix, accept_none=True)
        self.set_message(message, accept_none=True)
        self.set_log_level(log_level, accept_none=True)
        self.set_include_traceback(include_traceback, accept_none=True)
        self.set_blank_line(blank_line, accept_none=True)
        self.set_raise_exception(raise_exception, accept_none=True)
        self.set_actions(actions, accept_none=True)

    @staticmethod
    def _accept_none_check(accept_none):
        if not accept_none:
            raise ValueError("Nebyl předán parametr potřebný pro výpočet")

    def set_exception(self, exception: Type[Exception], accept_none=False):
        """Nastaví prefix pro zprávy logu."""
        if exception:
            verify(exception, Type[Exception])
            self.exception = exception
            return self
        self._accept_none_check(accept_none)


    def set_prefix(self, prefix: str, accept_none=False):
        """Nastaví prefix pro zprávy logu."""
        if prefix:
            verify(prefix, str)
            self.prefix = prefix
            return self
        self._accept_none_check(accept_none)


    def set_message(self, message: str, accept_none=False):
        """Nastaví základní zprávu pro log."""
        if message:
            verify(message, str)
            self.message = message
            return self
        self._accept_none_check(accept_none)

    @verify_entry
    def set_message(self, message: str, accept_none=False):
        """Nastaví základní zprávu pro log."""
        self.message = message
        return self



    def set_log_level(self, log_level: Union[int, str], accept_none=False):
        """Nastaví úroveň logování."""
        if log_level:
            verify(log_level, Union[int, str])
            self.log_level = log_level
            return self
        self._accept_none_check(accept_none)


    def set_include_traceback(self, include_traceback: bool, accept_none=False):
        """Nastaví, zda má být zahrnut traceback do logu."""
        if include_traceback:
            verify(include_traceback, bool)
            self.include_traceback = include_traceback
            return self
        self._accept_none_check(accept_none)


    def set_blank_line(self, blank_line: bool, accept_none=False):
        """Nastaví, zda má být přidán prázdný řádek na konec logu."""
        if blank_line:
            verify(blank_line, bool)
            self.blank_line = blank_line
            return self
        self._accept_none_check(accept_none)


    def set_raise_exception(self, raise_exception: bool, accept_none=False):
        """Nastaví, zda má být výjimka znovu vyvolána."""
        if raise_exception:
            verify(raise_exception, bool)
            self.raise_exception = raise_exception
            return self
        self._accept_none_check(accept_none)


    def add_action(self, action: Callable, accept_none=False):
        """Přidá akci, která se má provést při zpracování výjimky."""
        if action:
            verify(action, Callable)
            if callable(action):
                self.actions.append(action)
            else:
                raise TypeError("Akce musí být volatelná funkce nebo metoda.")
            return self
        self._accept_none_check(accept_none)


    def set_actions(self, actions: List[Callable], accept_none=False):
        """Nastaví seznam akcí, které se mají provést při zpracování výjimky."""
        if actions:
            verify(actions, List[Callable])
            if not all(callable(action) for action in actions):
                raise TypeError(
                    "Všechny akce musí být volatelné funkce nebo metody.")
            self.actions = list(actions)
            return self
        self._accept_none_check(accept_none)
