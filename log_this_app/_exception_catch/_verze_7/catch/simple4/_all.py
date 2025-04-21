import logging
import traceback
from typing import Dict, List, Optional, Type, Union, Callable, Any, Set
from copy import deepcopy


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


class ExceptionConfig:
    """Konfigurační třída pro správu chování zpracování výjimek."""

    # Globální instance pro sdílené nastavení
    _global_instance = None

    def __init__(
            self,
            logger=None,
            log_level=logging.ERROR,
            log_file_path=None,
            log_format=None,
            prefix="[CATCH]",
            message="Chyba při vykonávání",
            include_traceback=True,
            blank_line=True,
            raise_exception=True,
            actions=None
    ):
        # Nastavení logování
        self.logger = logger or logging.getLogger()
        self.log_level = log_level
        self.log_file_path = log_file_path
        self.log_format = log_format

        # Nastavení formátu výstupu
        self.prefix = prefix
        self.message = message
        self.include_traceback = include_traceback
        self.blank_line = blank_line
        self.raise_exception = raise_exception
        self.actions = actions or []

        # Slovník pro specifická nastavení výjimek
        self.exception_handlers: Dict[
            Type[Exception], ExceptionHandlerSettings] = {}

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

    def copy(self):
        """Vytvoří kopii této konfigurace."""
        # Vytvoření mělké kopie
        new_config = ExceptionConfig(
            logger=self.logger,
            log_level=self.log_level,
            log_file_path=self.log_file_path,
            log_format=self.log_format,
            prefix=self.prefix,
            message=self.message,
            include_traceback=self.include_traceback,
            blank_line=self.blank_line,
            raise_exception=self.raise_exception,
            actions=self.actions.copy()
        )

        # Kopírování nastavení pro konkrétní výjimky
        for exc_type, settings in self.exception_handlers.items():
            new_config.exception_handlers[exc_type] = deepcopy(settings)

        return new_config

    def set_handler_for_exc(self, *exception_types):
        """
        Vytvoří nebo vrátí nastavení pro konkrétní typ výjimky.

        Args:
            *exception_types: Typy výjimek, pro které se má vytvořit nastavení

        Returns:
            ExceptionHandlerSettings pro první zadaný typ výjimky
        """
        result = None

        for exc_type in exception_types:
            if not issubclass(exc_type, BaseException):
                raise TypeError(f"{exc_type} není platná výjimka")

            # Pokud nastavení pro tento typ výjimky ještě neexistuje, vytvoř ho
            if exc_type not in self.exception_handlers:
                settings = ExceptionHandlerSettings(
                    exception_type=exc_type,
                    prefix=self.prefix,
                    message=self.message,
                    log_level=self.log_level,
                    include_traceback=self.include_traceback,
                    blank_line=self.blank_line,
                    raise_exception=self.raise_exception,
                    actions=self.actions.copy()
                )
                self.exception_handlers[exc_type] = settings

            # Pro první výjimku vrať nastavení
            if result is None:
                result = self.exception_handlers[exc_type]

        return result

    def get_settings_for_exception(self, exception):
        """
        Vrátí nastavení pro konkrétní výjimku.

        Args:
            exception: Instance výjimky nebo třída výjimky

        Returns:
            Tuple obsahující hodnoty pro zpracování výjimky
        """
        # Získej typ výjimky
        if isinstance(exception, type) and issubclass(exception, BaseException):
            exc_type = exception
        else:
            exc_type = exception.__class__

        # Pokud existuje specifické nastavení pro tento typ výjimky, použij ho
        handler_settings = self.exception_handlers.get(exc_type)

        if handler_settings:
            # Vytvoř slovník s hodnotami z nastavení pro konkrétní výjimku
            settings = {
                'prefix': handler_settings.prefix or self.prefix,
                'message': handler_settings.message or self.message,
                'log_level': handler_settings.log_level or self.log_level,
                'include_traceback': handler_settings.include_traceback if handler_settings.include_traceback is not None else self.include_traceback,
                'blank_line': handler_settings.blank_line if handler_settings.blank_line is not None else self.blank_line,
                'raise_exception': handler_settings.raise_exception if handler_settings.raise_exception is not None else self.raise_exception,
                'actions': handler_settings.actions
            }
        else:
            # Použij výchozí nastavení
            settings = {
                'prefix': self.prefix,
                'message': self.message,
                'log_level': self.log_level,
                'include_traceback': self.include_traceback,
                'blank_line': self.blank_line,
                'raise_exception': self.raise_exception,
                'actions': self.actions
            }

        return settings

    @classmethod
    def set_global_config(cls, config):
        """Nastaví globální konfiguraci pro všechny handlery."""
        if not isinstance(config, cls):
            raise TypeError(f"Konfigurace musí být instancí {cls.__name__}")
        cls._global_instance = config

    @classmethod
    def get_global_config(cls):
        """Získá globální konfiguraci, nebo vytvoří novou s výchozími hodnotami."""
        if cls._global_instance is None:
            cls._global_instance = cls()
        return cls._global_instance


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

        # Získej nastavení pro daný typ výjimky
        settings = config.get_settings_for_exception(exception)

        # Proveď definované akce
        self._execute_actions(settings['actions'])

        # Loguj výjimku, pokud je to požadováno
        if settings['log_level'] != "NO_LOGS":
            self._log_exception(exception, func, settings)

        # Znovu vyvolej výjimku, pokud je to požadováno
        if settings['raise_exception']:
            raise

    def _execute_actions(self, actions):
        """Provede definované akce."""
        for action in actions:
            try:
                action()
            except Exception as e:
                # Loguj chybu při provádění akce, ale nepřeruš zpracování
                self.config.logger.error(f"Chyba při provádění akce: {e}")

    def _log_exception(self, exception, func, settings):
        """Zaloguje výjimku podle nastavení."""
        log_message = self._format_log_message(exception, func, settings)
        self.config.logger.log(settings['log_level'], log_message)

        # Pokud je požadováno logování do souboru, ulož log
        if self.config.log_file_path:
            self._save_log_to_file(log_message)

    def _format_log_message(self, exception, func, settings):
        """Formátuje zprávu logu podle nastavení."""
        # Základní zpráva
        prefix = settings['prefix']
        message = settings['message']
        func_name = func.__name__
        exc_name = exception.__class__.__name__
        exc_description = str(exception)

        log_message = f"{prefix} {message} {func_name}. {exc_name} - {exc_description}."

        # Přidání informací z tracebacku, pokud je to požadováno
        if settings['include_traceback']:
            log_message += "\n" + self._get_traceback_info(exception)

        # Přidání prázdného řádku na konec, pokud je to požadováno
        if settings['blank_line']:
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

    def _save_log_to_file(self, log_message):
        """Uloží log do souboru."""
        try:
            with open(self.config.log_file_path, 'a', encoding='utf-8') as f:
                f.write(log_message + "\n")
        except Exception as e:
            self.config.logger.error(f"Chyba při ukládání logu do souboru: {e}")


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
    # Nastavení globální konfigurace
    global_config = ExceptionConfig(
        prefix="[GLOBAL]",
        message="Chyba v",
        raise_exception=True
    )
    ExceptionConfig.set_global_config(global_config)

    # Vytvoření kopie globální konfigurace pro vlastní nastavení
    custom_config = ExceptionConfig.get_global_config().copy()

    # Nastavení specifického chování pro ValueError
    value_error_settings = custom_config.set_handler_for_exc(ValueError)
    value_error_settings.set_prefix("[VALUE_ERROR]") \
        .set_message("Neplatná hodnota v") \
        .set_raise_exception(False) \
        .add_action(lambda: print("Provedena akce pro ValueError"))

    # Nastavení společného chování pro více výjimek
    custom_config.set_handler_for_exc(TypeError, KeyError, AttributeError) \
        .set_prefix("[TYPE_ERROR]") \
        .set_message("Typová chyba v") \
        .set_include_traceback(False)


    @exception_catch(ValueError, TypeError, config=custom_config)
    def process_data(data):
        if not isinstance(data, (int, float)):
            raise TypeError(f"Očekáváno číslo, dostáno {type(data).__name__}")
        if data < 0:
            raise ValueError("Hodnota musí být kladné číslo")
        return data * 2


    # Test s různými typy výjimek
    print("Test s TypeError:")
    process_data("not a number")  # Vyvolá TypeError, ale zachytí se

    print("\nTest s ValueError:")
    result = process_data(-5)  # Vyvolá ValueError, zachytí se a nevyvolá znovu
    print(f"Pokračujeme po ValueError, result = {result}")