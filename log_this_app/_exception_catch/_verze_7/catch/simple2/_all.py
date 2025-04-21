import logging
from typing import Dict, List, Optional, Type, Union, Callable, Any


class ExceptionHandlerConfig:
    """Konfigurační třída pro správu chování dekorátoru exception_catch."""

    # Statická proměnná pro uchování globální instance
    _global_instance = None

    @classmethod
    def get_global_instance(cls) -> Optional['ExceptionHandlerConfig']:
        """Vrátí globální instanci, pokud existuje."""
        return cls._global_instance

    @classmethod
    def set_global_instance(cls, instance: 'ExceptionHandlerConfig') -> None:
        """Nastaví globální instanci konfigurace."""
        if cls._global_instance is not None:
            logging.warning(
                "Přepisování existující globální instance ExceptionHandlerConfig")
        cls._global_instance = instance

    def __init__(self, logger=None, log_to_file=False, log_file_path=None,
                 log_level=logging.ERROR, log_format=None,
                 exception_handlers=None):
        """
        Inicializace konfigurační třídy.

        Args:
            logger: Vlastní logger pro použití (pokud není zadán, použije se root logger)
            log_to_file: Zda logovat do souboru
            log_file_path: Cesta k souboru pro logování
            log_level: Výchozí úroveň logování
            log_format: Vlastní formát logování
            exception_handlers: Slovník {exception_type: handler_config} pro specifické zpracování výjimek
        """
        self.logger = logger or logging.getLogger()
        self.log_to_file = log_to_file
        self.log_file_path = log_file_path
        self.log_level = log_level

        # Nastavení formátu logování
        self.log_format = log_format or '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

        # Slovník pro specifické zpracování výjimek
        self.exception_handlers = exception_handlers or {}

        # Inicializace logování
        self._setup_logging()

    def _setup_logging(self):
        """Nastavení logování podle konfigurace."""
        # Základní nastavení
        handlers = []
        formatter = logging.Formatter(self.log_format)

        # Nastavení console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        handlers.append(console_handler)

        # Nastavení file handler, pokud je požadováno
        if self.log_to_file and self.log_file_path:
            file_handler = logging.FileHandler(self.log_file_path)
            file_handler.setFormatter(formatter)
            handlers.append(file_handler)

        # Nastavení loggeru
        if not self.logger.handlers:  # Přidáme handlery pouze pokud ještě žádné nemá
            for handler in handlers:
                self.logger.addHandler(handler)

        self.logger.setLevel(self.log_level)

    def add_exception_handler(self, exception_type: Type[Exception],
                              log_level: int = None,
                              message_prefix: str = None,
                              custom_formatter: logging.Formatter = None,
                              handle_func: Callable[
                                  [Exception, Any], None] = None) -> None:
        """
        Přidá konfigurace pro zpracování konkrétního typu výjimky.

        Args:
            exception_type: Typ výjimky
            log_level: Úroveň logování pro tuto výjimku
            message_prefix: Prefix zprávy pro logování
            custom_formatter: Vlastní formatter pro tuto výjimku
            handle_func: Vlastní funkce pro zpracování výjimky
        """
        if not issubclass(exception_type, BaseException):
            raise TypeError(f"{exception_type} není platná výjimka")

        self.exception_handlers[exception_type] = {
            'log_level': log_level or self.log_level,
            'message_prefix': message_prefix or '',
            'custom_formatter': custom_formatter,
            'handle_func': handle_func
        }

    def log_exception(self, func_name: str, exception: Exception,
                      specific_exceptions: List[
                          Type[Exception]] = None) -> None:
        """
        Loguje výjimku podle konfigurace.

        Args:
            func_name: Jméno funkce, kde došlo k výjimce
            exception: Zachycená výjimka
            specific_exceptions: Seznam typů výjimek, které byly zadány v dekorátoru
        """
        exc_type = type(exception)

        # Kontrola, zda existuje specifická konfigurace pro daný typ výjimky
        handler_config = None
        for exc_class in self.exception_handlers:
            if isinstance(exception, exc_class):
                handler_config = self.exception_handlers[exc_class]
                break

        if handler_config:
            # Použijeme specifickou konfiguraci
            log_level = handler_config.get('log_level', self.log_level)
            prefix = handler_config.get('message_prefix', '')
            custom_handle_func = handler_config.get('handle_func')

            error_message = f"{prefix}Chyba při vykonávání {func_name}: {exception}"

            # Pokud je k dispozici vlastní handle funkce, použijeme ji
            if custom_handle_func:
                custom_handle_func(exception, {'error_message': error_message,
                                               'function': func_name})
            else:
                self.logger.log(log_level, error_message, exc_info=True)
        else:
            # Použijeme výchozí konfiguraci
            error_message = f"Chyba při vykonávání {func_name}: {exception}"
            self.logger.error(error_message, exc_info=True)


def exception_catch(*exceptions, config: ExceptionHandlerConfig = None):
    """
    Dekorátor pro zachytávání specifikovaných výjimek a logování chyb.

    Args:
        *exceptions: Typy výjimek, které mají být zachyceny
        config: Volitelná instance ExceptionHandlerConfig pro lokální konfiguraci
    """
    # Kontrola platnosti výjimek
    for _exc in exceptions:
        if not issubclass(_exc, BaseException):
            raise TypeError(f"{_exc} není platná výjimka")

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Určení konfigurace k použití
            # 1. Lokální konfigurace (pokud je poskytnuta)
            # 2. Globální konfigurace (pokud existuje)
            # 3. Nová výchozí konfigurace
            handler_config = config
            if handler_config is None:
                global_config = ExceptionHandlerConfig.get_global_instance()
                if global_config:
                    handler_config = global_config
                else:
                    handler_config = ExceptionHandlerConfig()

            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Log a propagace výjimky podle konfigurace
                handler_config.log_exception(func.__name__, e,
                                             specific_exceptions=exceptions)
                raise

        return wrapper

    return decorator


# Příklad použití:
if __name__ == "__main__":
    # 1. Použití s výchozím nastavením (bez globální konfigurace)
    @exception_catch(ValueError, TypeError)
    def example_function_1(x):
        return 10 / x


    # 2. Vytvoření a nastavení globální konfigurace
    global_config = ExceptionHandlerConfig(
        log_to_file=True,
        log_file_path="errors.log",
        log_level=logging.WARNING
    )
    global_config.add_exception_handler(
        ZeroDivisionError,
        log_level=logging.CRITICAL,
        message_prefix="KRITICKÁ CHYBA: "
    )
    ExceptionHandlerConfig.set_global_instance(global_config)


    @exception_catch(ZeroDivisionError)
    def example_function_2(x):
        return 10 / x


    # 3. Použití s lokální konfigurací
    local_config = ExceptionHandlerConfig(
        log_level=logging.INFO
    )
    local_config.add_exception_handler(
        ZeroDivisionError,
        message_prefix="Lokální zpracování: "
    )


    @exception_catch(ZeroDivisionError, config=local_config)
    def example_function_3(x):
        return 10 / x


    # Testování
    try:
        example_function_1(0)  # Vyvolá ZeroDivisionError s výchozím nastavením
    except Exception as e:
        print(f"Zachyceno: {e}")

    try:
        example_function_2(0)  # Vyvolá ZeroDivisionError s globální konfigurací
    except Exception as e:
        print(f"Zachyceno: {e}")

    try:
        example_function_3(0)  # Vyvolá ZeroDivisionError s lokální konfigurací
    except Exception as e:
        print(f"Zachyceno: {e}")