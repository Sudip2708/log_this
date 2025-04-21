import traceback

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