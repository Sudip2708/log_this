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