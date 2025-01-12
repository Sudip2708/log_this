from typing import Any, Optional
from enum import Enum
import logging
import inspect
import functools


class LogLevel(Enum):
    DEV_DEBUG = 10
    DEV_ERROR = 40
    DEV_CRITICAL = 50
    USER_INFO = 20
    USER_WARNING = 30


class DevLogger:
    """Logger pro vývojáře s předpřipravenými metodami."""

    def __init__(self, name: str = "dev"):
        self.logger = LogManager.get_logger(f"LogThis.{name}", log_to_file=True)

    def enter(self, message: Optional[str] = None) -> None:
        """Loguje vstup do funkce/metody/modulu."""
        caller_frame = inspect.currentframe().f_back
        caller_info = inspect.getframeinfo(caller_frame)
        location = f"{caller_info.filename}:{caller_info.function}:{caller_info.lineno}"

        if message:
            self.logger.debug(f"ENTER {location} - {message}")
        else:
            self.logger.debug(f"ENTER {location}")

    def exit(self, result: Any = None) -> None:
        """Loguje výstup z funkce/metody/modulu."""
        caller_frame = inspect.currentframe().f_back
        caller_info = inspect.getframeinfo(caller_frame)
        location = f"{caller_info.filename}:{caller_info.function}:{caller_info.lineno}"

        if result is not None:
            self.logger.debug(f"EXIT {location} - Result: {result}")
        else:
            self.logger.debug(f"EXIT {location}")

    def var(self, **variables) -> None:
        """Loguje hodnoty proměnných."""
        for name, value in variables.items():
            self.logger.debug(f"VAR {name} = {value}")

    def step(self, step_name: str) -> None:
        """Loguje průběžný krok v procesu."""
        self.logger.debug(f"STEP {step_name}")

    def error(self, error: Exception, context: Optional[str] = None) -> None:
        """Loguje chybu s kontextem."""
        if context:
            self.logger.error(f"ERROR in {context}: {str(error)}")
        else:
            self.logger.error(f"ERROR: {str(error)}")


class UserLogger:
    """Logger pro komunikaci s uživatelem."""

    def __init__(self, name: str = "user"):
        self.logger = LogManager.get_logger(f"LogThis.{name}")

    def progress(self, step: str, total_steps: Optional[int] = None) -> None:
        """Informuje o průběhu operace."""
        if total_steps:
            self.logger.info(
                f"Progress: {step} ({total_steps} steps remaining)")
        else:
            self.logger.info(f"Progress: {step}")

    def success(self, message: str) -> None:
        """Oznamuje úspěšné dokončení operace."""
        self.logger.info(f"✓ {message}")

    def warning(self, message: str, suggestion: Optional[str] = None) -> None:
        """Varuje uživatele s možným návrhem řešení."""
        if suggestion:
            self.logger.warning(f"⚠ {message}\nSuggestion: {suggestion}")
        else:
            self.logger.warning(f"⚠ {message}")


# Příklad použití:
dev_log = DevLogger()
user_log = UserLogger()


def process_data(data: list) -> list:
    dev_log.enter()
    dev_log.var(input_length=len(data))

    user_log.progress("Processing data...")

    try:
        result = [x * 2 for x in data]
        dev_log.step("Data transformation completed")
        user_log.success("Data processed successfully")

        dev_log.var(output_length=len(result))
        dev_log.exit(result)
        return result

    except Exception as e:
        dev_log.error(e, "data processing")
        user_log.warning("Data processing failed", "Try with smaller dataset")
        raise


"""
Tento návrh zahrnuje:

Rozdělení na DevLogger a UserLogger pro jasné oddělení účelu
Předpřipravené metody pro běžné případy použití:

DevLogger:

enter/exit pro sledování toku programu
var pro logování proměnných
step pro logování kroků
error pro chyby s kontextem


UserLogger:

progress pro informování o průběhu
success pro oznámení úspěchu
warning pro varování s návrhy řešení




Jednoduché, ale informativní formátování výstupu

Toto je základní sada metod, kterou bych doporučil pro začátek. Je dostatečně kompletní pro běžné použití, ale není přehlcující. Později by se dalo rozšířit například o:

Měření času mezi enter/exit
Více formátů pro výpis proměnných
Automatické logování stacktrace při chybách
Agregaci souvisejících logů do skupin

Co si o tomto návrhu myslíš? Odpovídá to tvé představě o použitelnosti pro začátečníky?
"""