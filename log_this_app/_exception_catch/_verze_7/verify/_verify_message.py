from typing import Optional

from ._exceptions import SafeVerifyError


def _verify_message(message: Optional[str]) -> str:
    """
    Ověří platnost chybové zprávy.

    Args:
        message (Optional[str]): Zpráva k ověření.

    Returns:
        str: Ověřená zpráva.

    Raises:
        SafeVerifyError: Pokud zpráva nesplňuje požadavky.
    """
    try:

        # Převedení na řetězec (pro případ, že by někdo poslal něco jiného)
        message_str = str(message).strip()

        # Volitelné další kontroly, například maximální délka
        if len(message_str) > 500:  # Příklad omezení délky
            raise SafeVerifyError("Chybová zpráva je příliš dlouhá")

        # Kontrola znaků (volitelné)
        if not message_str:
            raise SafeVerifyError("Chybová zpráva nesmí být prázdná")

        return message_str

    except Exception as e:
        raise SafeVerifyError(
            f"Neočekávaná chyba funkce _verify_message. "
            f"{e.__class__.__name__}: {str(e)}")