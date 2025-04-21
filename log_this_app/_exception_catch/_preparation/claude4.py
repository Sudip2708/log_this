import inspect
from typing import Any, Callable, Optional, Type, Union


class SafeVerifyError(Exception):
    """Interní výjimka pro bezpečné ověřování."""
    pass


class ExceptionHandler:
    @classmethod
    def _safe_verify(
            cls,
            condition: Union[bool, Callable[[], bool]],
            message: Optional[str] = None,
            exception_type: Type[Exception] = SafeVerifyError
    ) -> bool:
        """
        Bezpečná interní metoda pro ověřování vstupů.

        :param condition: Podmínka k ověření (boolean nebo callable)
        :param message: Volitelná chybová zpráva
        :param exception_type: Typ výjimky (default SafeVerifyError)
        :return: True pokud je podmínka splněna
        :raises: Specifikovaná výjimka při selhání
        """
        try:
            # Pokud je condition callable, vyvolej ji
            check = condition() if callable(condition) else condition

            # Automatická tvorba zprávy
            if message is None:
                frame = inspect.currentframe().f_back
                caller_info = inspect.getframeinfo(frame)
                message = (
                    f"Ověření selhalo v metodě {caller_info.function} "
                    f"v souboru {caller_info.filename}:{caller_info.lineno}"
                )

            # Kontrola podmínky
            if not check:
                raise exception_type(message)

            return True

        except Exception as e:
            # Zachycení jakékoliv vnitřní chyby při ověřování
            raise SafeVerifyError(f"Chyba při ověřování: {str(e)}")

    def set_log_level(
            self,
            level: int,
            exception_type: Optional[type] = None
    ) -> 'ExceptionHandler':
        # Použití safe verify pro vstupní parametry
        self._safe_verify(
            lambda: isinstance(level, int),
            "Úroveň logování musí být celočíselná hodnota"
        )

        if exception_type:
            self._safe_verify(
                lambda: isinstance(exception_type, type),
                "Typ výjimky musí být platný typ"
            )

        # Původní logika metody...
        if exception_type:
            self._log_levels[exception_type] = level
        else:
            self._default_log_level = level
        return self

    def set_message(
            self,
            message: str,
            exception_type: Optional[type] = None
    ) -> 'ExceptionHandler':
        # Ověření vstupních parametrů
        self._safe_verify(
            lambda: isinstance(message, str),
            "Zpráva musí být řetězec"
        )

        if exception_type:
            self._safe_verify(
                lambda: isinstance(exception_type, type),
                "Typ výjimky musí být platný typ"
            )

        # Původní logika metody...
        if exception_type:
            self._custom_messages[exception_type] = message
        else:
            self._custom_messages[Exception] = message
        return self


# Příklad použití
def example():
    handler = ExceptionHandler()

    # Bezpečné volání metod s ověřením vstupů
    handler.set_log_level(logging.ERROR)
    handler.set_message("Chybová zpráva")

    # Vyvolání vnitřní výjimky při neplatném vstupu
    try:
        handler.set_log_level("neplatná hodnota")
    except SafeVerifyError as e:
        print(f"Zachycena bezpečnostní výjimka: {e}")