from typing import Dict, List, Optional, Type, Union, Callable, Any, Set


class ExceptionHandlerSettings:
    """Datová třída pro nastavení zpracování konkrétního typu výjimky."""

    def __init__(
            self,
            exception_type: Type[Exception],
            prefix: str = None,
            message: str = None,
            log_level: Union[int, str] = None,
            include_traceback: bool = None,
            blank_line: bool = None,
            raise_exception: bool = None,
            actions: List[Callable] = None
    ):
        self.exception_type = exception_type
        self.prefix = prefix
        self.message = message
        self.log_level = log_level
        self.include_traceback = include_traceback
        self.blank_line = blank_line
        self.raise_exception = raise_exception
        self.actions = actions or []

    def set_prefix(self, prefix: str):
        """Nastaví prefix pro zprávy logu."""
        self.prefix = prefix
        return self

    def set_message(self, message: str):
        """Nastaví základní zprávu pro log."""
        self.message = message
        return self

    def set_log_level(self, log_level: Union[int, str]):
        """Nastaví úroveň logování."""
        self.log_level = log_level
        return self

    def set_include_traceback(self, include_traceback: bool):
        """Nastaví, zda má být zahrnut traceback do logu."""
        self.include_traceback = include_traceback
        return self

    def set_blank_line(self, blank_line: bool):
        """Nastaví, zda má být přidán prázdný řádek na konec logu."""
        self.blank_line = blank_line
        return self

    def set_raise_exception(self, raise_exception: bool):
        """Nastaví, zda má být výjimka znovu vyvolána."""
        self.raise_exception = raise_exception
        return self

    def add_action(self, action: Callable):
        """Přidá akci, která se má provést při zpracování výjimky."""
        if callable(action):
            self.actions.append(action)
        else:
            raise TypeError("Akce musí být volatelná funkce nebo metoda.")
        return self

    def set_actions(self, actions: List[Callable]):
        """Nastaví seznam akcí, které se mají provést při zpracování výjimky."""
        if not all(callable(action) for action in actions):
            raise TypeError(
                "Všechny akce musí být volatelné funkce nebo metody.")
        self.actions = list(actions)
        return self