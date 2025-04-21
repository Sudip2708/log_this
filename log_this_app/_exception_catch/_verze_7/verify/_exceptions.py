class VerifyError(Exception):
    """
    Vlastní výjimka pro selhání ověřovacích kontrol.

    Args:
        message (str): Detailní popis důvodu selhání ověření.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class SafeVerifyError(Exception):
    """
    Interní výjimka pro bezpečné zachytávání chyb během ověřování.

    Args:
        message (str): Interní chybová zpráva zachycující technické detaily selhání.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)