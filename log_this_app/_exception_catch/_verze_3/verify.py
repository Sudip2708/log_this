from typing import Optional, Type
import inspect


class VerifyError(Exception):
    """Vlastní výjimka pro selhání ověření."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


def verify(
        condition: bool,
        message: Optional[str] = None,
        exception_type: Type[Exception] = VerifyError
) -> bool:
    """
    Universální metoda pro ověřování podmínek.

    :param condition: Podmínka k ověření
    :param message: Volitelná vlastní chybová zpráva
    :param exception_type: Typ výjimky (defaultně VerifyError)
    :return: True pokud je podmínka splněna
    :raises: Specifikovaná výjimka pokud podmínka selhá

    Ukázka použití:
        try:
            verify(isinstance("text", str), "Musí být řetězec")
            verify(5 > 3, "Neplatná matematická podmínka")
        except VerifyError as e:
            print(f"Ověření selhalo: {e}")
    """

    # Zjištění kontextu volání
    frame = inspect.currentframe().f_back
    caller_info = inspect.getframeinfo(frame)

    # Automatická tvorba zprávy pokud není poskytnuta
    if message is None:
        message = (
            f"Ověření selhalo v metodě {caller_info.function} "
            f"v souboru {caller_info.filename}:{caller_info.lineno}"
        )

    # Pokud podmínka nesplněna, vyvolej výjimku
    if not condition:
        raise exception_type(message)

    return True


