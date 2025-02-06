from typing import Any, Optional
from enum import Enum
import logging
from functools import partial

from .manager_old import LocalManager, logger_settings

# Získání instance manažera a loggeru
manager = LocalManager()
logger = logger_settings()


class LogLevel(Enum):
    """Výčet podporovaných úrovní logování."""
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


def _format_message(message: Any, level: Optional[LogLevel] = None) -> str:
    """
    Formátuje zprávu pro výpis v konzistentním stylu s dekorátorem log_this.

    Args:
        message: Zpráva k naformátování
        level: Úroveň logování pro případné přidání prefixu

    Returns:
        str: Naformátovaná zpráva
    """
    # Získání aktuálního odsazení
    indent = manager.get_indent()

    # Serializace zprávy na string
    msg = str(message)

    # Přidání prefixu úrovně logování, pokud je specifikována
    if level:
        msg = f"[{level.name}] {msg}"

    # Aplikace odsazení na každý řádek zprávy
    formatted_lines = [f"{indent}{line}" for line in msg.split('\n')]
    return '\n'.join(formatted_lines)


def _log_with_context(message: Any, level: Optional[LogLevel] = None) -> None:
    """
    Vypisuje zprávu s kontextem odsazení a prázdných řádků.

    Args:
        message: Zpráva k vypsání
        level: Úroveň logování
    """
    try:
        # Aktualizace kontextu pro správné odsazení
        manager.update_context(
            mode=1)  # Použijeme mode 1 pro konzistenci s jednořádkovým výpisem

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
            logger.debug(formatted_msg)

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
    _log_with_context(message)


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