import logging

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

