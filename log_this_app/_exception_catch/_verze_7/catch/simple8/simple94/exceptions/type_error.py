from ._verify_error import VerifyError


class VerifyTypeError(VerifyError, TypeError):
    """Výjimka vyvolaná při neplatném ověření hodnoty."""