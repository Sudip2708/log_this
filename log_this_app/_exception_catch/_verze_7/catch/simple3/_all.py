import logging
import traceback
from typing import Dict, List, Optional, Type, Union, Callable, Any, Set


class ExceptionConfig:
    """Konfigurační třída pro správu chování zpracování výjimek."""

    # Globální instance pro sdílené nastavení
    global_instance = None

    def __init__(
            self,
            logger=None,
            log_level=logging.ERROR,
            log_file_path=None,
            log_format=None,
            exception_handlers=None,
            actions=None,
            prefix="[CATCH]",
            message="Chyba při vykonávání",
            include_traceback=True,
            blank_line=True,
            raise_exception=True,
    ):
        # Nastavení logování
        self.logger = logger or logging.getLogger()
        self.log_level = log_level
        self.log_file_path = log_file_path
        self.log_format = log_format

        # Nastavení pro zpracování výjimek
        self.exception_handlers = exception_handlers or {}
        self.actions = actions or []

        # Nastavení formátu výstupu
        self.prefix = prefix
        self.message = message
        self.include_traceback = include_traceback
        self.blank_line = blank_line
        self.raise_exception = raise_exception

        # Inicializace logování pokud je to potřeba
        if log_file_path:
            self._setup_logging()

    def _setup_logging(self):
        """Nastavení logování do souboru, pokud je to požadováno."""
        if self.log_file_path:
            file_handler = logging.FileHandler(self.log_file_path)
            if self.log_format:
                formatter = logging.Formatter(self.log_format)
                file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_config_for_exception(self, exception_type):
        """Vrátí specifickou konfiguraci pro daný typ výjimky, pokud existuje."""
        return self.exception_handlers.get(exception_type, self)

    @classmethod
    def set_global_config(cls, config):
        """Nastaví globální konfiguraci pro všechny handlery."""
        if not isinstance(config, cls):
            raise TypeError(f"Konfigurace musí být instancí {cls.__name__}")
        cls.global_instance = config

    @classmethod
    def get_global_config(cls):
        """Získá globální konfiguraci, nebo vytvoří novou s výchozími hodnotami."""
        if cls.global_instance is None:
            cls.global_instance = cls()
        return cls.global_instance


class ExceptionHandler:
    """Třída pro zpracování zachycených výjimek."""

    def __init__(self, config=None):
        """
        Inicializace handleru výjimek.

        Args:
            config: Instance ExceptionConfig pro konfiguraci zpracování výjimek
        """
        self.config = config or ExceptionConfig.get_global_config()

    def handle_exception(self, exception, func, config=None):
        """
        Zpracuje zachycenou výjimku podle konfigurace.

        Args:
            exception: Zachycená výjimka
            func: Funkce, ve které výjimka nastala
            config: Volitelná lokální konfigurace, která přepíše globální nastavení
        """
        # Použij lokální konfiguraci, pokud je poskytnuta
        config = config or self.config

        # Získej specifickou konfiguraci pro daný typ výjimky
        exc_type = exception.__class__
        exc_config = config.get_config_for_exception(exc_type)

        # Proveď definované akce
        self._execute_actions(exc_config)

        # Loguj výjimku, pokud je to požadováno
        if exc_config.log_level != "NO_LOGS":
            self._log_exception(exception, func, exc_config)

        # Znovu vyvolej výjimku, pokud je to požadováno
        if exc_config.raise_exception:
            raise

    def _execute_actions(self, config):
        """Provede definované akce z konfigurace."""
        for action in config.actions:
            try:
                action()
            except Exception as e:
                # Loguj chybu při provádění akce, ale nepřeruš zpracování
                config.logger.error(f"Chyba při provádění akce: {e}")

    def _log_exception(self, exception, func, config):
        """Zaloguje výjimku podle konfigurace."""
        log_message = self._format_log_message(exception, func, config)
        config.logger.log(config.log_level, log_message)

        # Pokud je požadováno logování do souboru, ulož log
        if config.log_file_path:
            self._save_log_to_file(log_message, config)

    def _format_log_message(self, exception, func, config):
        """Formátuje zprávu logu podle konfigurace."""
        # Základní zpráva
        prefix = config.prefix
        message = config.message
        func_name = func.__name__
        exc_name = exception.__class__.__name__
        exc_description = str(exception)

        log_message = f"{prefix} {message} {func_name}. {exc_name} - {exc_description}."

        # Přidání informací z tracebacku, pokud je to požadováno
        if config.include_traceback:
            log_message += "\n" + self._get_traceback_info(exception)

        # Přidání prázdného řádku na konec, pokud je to požadováno
        if config.blank_line:
            log_message += "\n"

        return log_message

    def _get_traceback_info(self, exception):
        """Získá informace z tracebacku výjimky."""
        tb = traceback.extract_tb(exception.__traceback__)

        # Poslední a první frame z tracebacku
        last_frame = tb[-1]
        first_frame = tb[0] if len(tb) > 1 else None

        # Informace o místě výjimky
        filename = last_frame.filename
        line_number = last_frame.lineno
        line_code = last_frame.line

        result = f"Soubor: {filename}, řádek: {line_number}, kód: {line_code}."

        # Přidej informace o původu výjimky, pokud je k dispozici
        if first_frame and first_frame != last_frame:
            origin = f"Původ: {first_frame.filename}, řádek: {first_frame.lineno}, kód: {first_frame.line}."
            result += f" {origin}"

        return result

    def _save_log_to_file(self, log_message, config):
        """Uloží log do souboru."""
        try:
            with open(config.log_file_path, 'a', encoding='utf-8') as f:
                f.write(log_message + "\n")
        except Exception as e:
            config.logger.error(f"Chyba při ukládání logu do souboru: {e}")


def exception_catch(*exceptions, config=None):
    """
    Dekorátor pro zachytávání specifikovaných výjimek a logování chyb.

    Args:
        *exceptions: Typy výjimek, které mají být zachyceny (pokud prázdné, zachytí všechny)
        config: Volitelná instance ExceptionConfig pro lokální konfiguraci
    """
    # Validace výjimek
    for exc in exceptions:
        if not issubclass(exc, BaseException):
            raise TypeError(f"{exc} není platná výjimka")

    # Vytvoření výchozího handleru
    handler = ExceptionHandler(config)

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Pokud byly specifikovány výjimky a aktuální výjimka není v seznamu, nechej ji projít
                if exceptions and not any(
                        isinstance(e, exc) for exc in exceptions):
                    raise

                # Jinak zpracuj výjimku
                handler.handle_exception(e, func, config)

        return wrapper

    return decorator


# Příklad použití:
if __name__ == "__main__":
    # Globální konfigurace
    global_config = ExceptionConfig(
        prefix="[GLOBAL]",
        message="Chyba v",
        raise_exception=True
    )
    ExceptionConfig.set_global_config(global_config)

    # Lokální konfigurace pro konkrétní dekorátor
    db_config = ExceptionConfig(
        prefix="[DB]",
        message="Database error in",
        raise_exception=False
    )


    @exception_catch(ValueError, TypeError)
    def process_data(data):
        # Kód, který může vyvolat výjimku
        result = data * 2
        return result


    @exception_catch(Exception, config=db_config)
    def save_to_database(data):
        # Simulace chyby databáze
        raise ConnectionError("Could not connect to database")


    try:
        process_data("not a number")  # Vyvolá TypeError
    except Exception as e:
        print(f"Caught: {e}")

    save_to_database("data")  # Výjimku nevyvolá zpět díky db_config