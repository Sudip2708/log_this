from typing import Any, Optional
from enum import Enum
import logging
from datetime import datetime
import inspect
from functools import partial

from .manager_old import LocalManager, logger_settings
from .utils import safe_serialize

# Získání instance manažera a loggeru
manager = LocalManager()
logger = logger_settings()


class LogLevel(Enum):
    """Výčet podporovaných úrovní logování."""
    NOTE = (logging.DEBUG, "NOTE")
    DEBUG = (logging.DEBUG, "DEBUG")
    INFO = (logging.INFO, "INFO")
    WARNING = (logging.WARNING, "WARNING")
    ERROR = (logging.ERROR, "ERROR")
    CRITICAL = (logging.CRITICAL, "CRITICAL")

    def __init__(self, level: int, label: str):
        self.level = level
        self.label = label


def _get_caller_info() -> tuple:
    """
    Získá informace o volajícím (funkce/metoda, třída, číslo řádku).

    Returns:
        tuple: (název volajícího, číslo řádku)
    """
    # Získání frame volajícího
    frame = inspect.currentframe()
    try:
        # Přeskočení interních funkcí a získání frame volajícího
        frame = frame.f_back.f_back.f_back

        # Získání informací o volajícím
        code = frame.f_code
        calling_file = code.co_filename
        line_no = frame.f_lineno

        # Pokus o získání názvu třídy (pokud existuje)
        if 'self' in frame.f_locals:
            class_name = frame.f_locals['self'].__class__.__name__
            return f"{class_name}.{code.co_name}", line_no

        return code.co_name, line_no
    finally:
        del frame  # Vyčištění reference na frame


def _format_message(message: Any, level: Optional[LogLevel] = None) -> str:
    """
    Formátuje zprávu pro výpis v konzistentním stylu.

    Args:
        message: Zpráva k naformátování
        level: Úroveň logování

    Returns:
        str: Naformátovaná zpráva
    """
    # Získání aktuálního odsazení a informací o volajícím
    indent = manager.get_indent()
    caller_name, line_no = _get_caller_info()

    # Příprava časového razítka
    timestamp = datetime.now()

    # Serializace zprávy
    msg = safe_serialize(message)

    # Sestavení hlavičky logu
    header = (
        f"{indent}# {level.label} LogThis('{level.label.lower() if level else 'log'}') "
        f"| {timestamp} "
        f"| {caller_name}:{line_no}"
    )

    # Sestavení těla zprávy
    message_body = f"{indent}# >>> MESSAGE: {msg}"

    return f"{header}\n{message_body}"


def _log_with_context(message: Any, level: Optional[LogLevel] = None) -> None:
    """
    Vypisuje zprávu s kontextem odsazení a prázdných řádků.

    Args:
        message: Zpráva k vypsání
        level: Úroveň logování
    """
    try:
        # Aktualizace kontextu pro správné odsazení
        manager.update_context(mode=1)  # Jednořádkový mód

        # Získání počtu prázdných řádků
        start_blank, end_blank = manager.get_blank_lines()

        # Výpis prázdných řádků před zprávou
        if start_blank:
            print('\n' * start_blank, end='')

        # Formátování a výpis zprávy
        formatted_msg = _format_message(message, level)

        # Výpis podle úrovně logování
        if level:
            getattr(logger, level.name.lower())(formatted_msg)
        else:
            logger.info(formatted_msg)

        # Výpis prázdných řádků po zprávě
        if end_blank:
            print('\n' * end_blank, end='')

    finally:
        # Obnovení původního kontextu
        manager.revert_context()


# Základní logovací funkce
def log(message: Any) -> None:
    """
    Vypíše zprávu ve stylu knihovny log_this.

    Args:
        message: Zpráva k vypsání
    """
    _log_with_context(message, LogLevel.NOTE)


# Specializované logovací funkce
def log_debug(message: Any) -> None:
    """Vypíše debug zprávu."""
    _log_with_context(message, LogLevel.DEBUG)


def log_info(message: Any) -> None:
    """Vypíše informační zprávu."""
    _log_with_context(message, LogLevel.INFO)


def log_warning(message: Any) -> None:
    """Vypíše varovnou zprávu."""
    _log_with_context(message, LogLevel.WARNING)


def log_error(message: Any) -> None:
    """Vypíše chybovou zprávu."""
    _log_with_context(message, LogLevel.ERROR)


def log_critical(message: Any) -> None:
    """Vypíše kritickou zprávu."""
    _log_with_context(message, LogLevel.CRITICAL)