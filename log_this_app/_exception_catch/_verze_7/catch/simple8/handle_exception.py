import inspect
from functools import wraps
from typing import Dict, List, Optional, Type, Union, Callable, Any, Set, get_type_hints

from .handle_exception_constants import HandleExceptionConstants


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