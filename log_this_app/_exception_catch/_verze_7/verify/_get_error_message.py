import inspect
from typing import Optional

from ._exceptions import SafeVerifyError
from ._verify_message import _verify_message


def _get_error_message(
        message: Optional[str] = None,
) -> str:  # Falešné hlášení: návratová hodnota je vždy `str`, ale statická analýza bere v úvahu `finally`, která jen čistí případný frame
    """
    Generování kontextové chybové zprávy.

    Args:
        message (Optional[str], optional): Volitelná uživatelská chybová zpráva.

    Returns:
        str: Detailní chybová zpráva.

    Raises:
        SafeVerifyError: Při problémech s extrakcí kontextových informací.
    """
    try:
        # Preferovaná uživatelská zpráva
        if message:
            return _verify_message(message)

        # Extrakce informací o volání
        frame = inspect.currentframe()
        try:
            caller_frame = frame.f_back
            if caller_frame:
                caller_info = inspect.getframeinfo(caller_frame)
                return (
                    f"Ověření selhalo v metodě {caller_info.function} "
                    f"v souboru {caller_info.filename}:{caller_info.lineno}"
                )
            return "Ověření selhalo v neznámém kontextu"

        finally:
            # Explicitní smazání reference na frame (pro případ cyklické reference)
            if frame:
                del frame

    except Exception as e:
        raise SafeVerifyError(
            f"Neočekávaná chyba funkce _get_error_message. "
            f"{e.__class__.__name__}: {str(e)}"
        )