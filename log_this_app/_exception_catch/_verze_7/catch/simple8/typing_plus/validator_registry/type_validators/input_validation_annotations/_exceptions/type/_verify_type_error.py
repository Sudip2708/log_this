from ._verify_error import VerifyError

class VerifyTypeError(VerifyError, TypeError):
    """Bázová třída pro chyby týkající se typů."""