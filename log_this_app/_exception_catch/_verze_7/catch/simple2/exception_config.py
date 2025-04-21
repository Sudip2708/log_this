import logging
from typing import Dict, List, Optional, Type, Union, Callable, Any

class ExceptionConfig:
    """Konfigurační třída pro správu chování dekorátoru exception_catch."""

    # Atribut pro uchování instance s vlastním globáním nastavení
    global_instance = None

    # Atribut pro slovník schromažďující nastavení pro konkrétní typi výjimek
    exception_handlers = {}

    # Atribut pro slovník akcí, které se mají provést při každém úkonu
    action = {}

    # Atribut pro navázení logera pro vyřízení log požadavků
    loger = None
    # Atribut uchovávající level logování (Umožňuje i zadání NoLOG pro nelogování)
    log_level = logging.ERROR
    # Atribut odkazující na cestu pro ukládání logů (Neníli zadaný k ukládání logu nedochází)
    log_file_path = None
    # Atribut definující základní konstrukci
    log_format = None


    # Atribut pro nastavení textu zobrazujícího se před hlavní zprávou
    prefix = "[CATCH]"
    # Atribut pro nastavení řádku oznamu zprávy logu
    message = ""
    # Atribut pro řádek s doplňujícími informacemi
    specification = ""
    # Boolean atribut definující zda má být za oznamem oddělující prázdný řádek (pro lepší orientaci)
    blank_line = True
    # Boolean atribut definující zda se má po zalogování vyvolat i výjimka
    raise_exception = True

    def __init__(
            self,

            logger=None,
            log_level=logging.ERROR,
            log_file_path=None,
            log_format=None,

            action=None,

            prefix=None,
            message=None,
            specification=None,

            blank_line=True,
            raise_exception=True,

    ):
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
        # Nastavení logeru
        self.logger = logger or logging.getLogger()
        self.log_level = log_level
        self.log_file_path = log_file_path or self.log_file_path
        self.log_format = log_format or self.log_format

        # Nastavení akce
        self.action = action or self.action

        # Nastavení pro výstup
        self.prefix = prefix
        self.message = message
        self.specification = specification

        self.blank_line = blank_line
        self.raise_exception = raise_exception

        # Inicializace logování
        self._setup_logging()

    @staticmethod
    def get_exception_mane(exception):
        return exception.__class__.__name__

    @staticmethod
    def verify_config(config):
        if not isinstance(config, ExceptionConfig):
            raise ValueError("Předaná konfigurace není platnou konfigurací")

    def get_config(self, config):
        if config:
            self.verify_config(config)
            return config
        return self.global_instance if self.global_instance else self.default_settings

    def get_exception_config(self, exception_mane, config):
        config = self.get_config(config)
        if exception_mane in config.exception_handlers:
            return config.get_config_for_exception(exception_mane)
        return config

    @staticmethod
    def check_and_do_actions(config):
        if config.actions:
            # Projití a vykonání seznamu akcí
            for action in config.actions:
                action()

    @staticmethod
    def get_log_message(exc_config, exception, func):
        # Vytvoření zprávy
        prefix = exc_config.prefix  # "[DB]"
        message = exc_config.message  # "Chyba při vykonávání "
        func_name = func.__name__  # "moje_funkce"

        # Přepis výjimky
        exc_name = exception.__class__.__name__
        exc_description = str(exception)

        return (
            f"{prefix} {message} {func_name}. "
            f"{exc_name} - {exc_description}. \n"
        )

    @staticmethod
    def get_traceback_info(exc_config, exception):
        # Doplňující informace
        # Načtení traceback u
        tb = traceback.extract_tb(exception.__traceback__)
        last_frame = tb[-1]  # Poslední krok v tracebacku (tato funkce)
        first_frame = tb[0] if len(tb) > 1 else ""  # Původ výjimky

        # Definice textu
        filename = last_frame.filename  # "muj_soubor.py"
        line_number = last_frame.lineno  # 15
        line_code = last_frame.line  # "return 10 / 0"

        # Definice doplňujícího textu o počátku chyby
        origin = ""
        if first_frame:
            or_filename = last_frame.filename  # "muj_soubor.py"
            or_line_number = last_frame.lineno  # 15
            or_line_code = last_frame.line  # "return 10 / 0"
            origin = f"Původ: {or_filename}, řádek: {or_line_number}, kód: {or_line_code}. \n"

        # Definice ukončení
        end = '\n' if exc_config.blank_line else ''

        return (
            f"Soubor: {filename}, řádek: {line_number}, kód: {line_code}. "
            f"{origin}.{end}\n"
        )

    def get_log(self, exc_config, exception, func):
        if exc_config.log_format:
            return self.get_log_for_log_format(exception, func)

        log_message = self.get_log_message(exc_config, exception, func)

        if exc_config.traceback_info:
            log_message += self.get_traceback_info(exc_config, exception)

        return log_message


    def handle_exception(self, exception, func, config):

        # Načtení jména výjimky
        exc_mane = self.get_exception_mane(exception)

        # Načtení konfigurace pro danou výjimku
        exc_config = self.get_exception_config(exc_mane, config)

        # Kontrola, zda jsou nastavené nějaké akce
        self.check_and_do_actions(exc_config)

        # Kontrola zda se má vypsat log
        if exc_config.log_level != "NO_LOGS":
            exc_config.logger.log(
                exc_config.log_level,
                exc_config.get_log(exc_config, exception, func)
            )

        # Kontrola, zda se má vypsat i do souboru
        if exc_config.log_file_path:
            exc_config.save_log_to_file()

        # Kontrola zda je nastaveno že se nemá vyvolat výjimka
        if exc_config.raise_exception:
            raise




