from typing import Optional

class ExitInteractiveMode(Exception):
    """Výjimka signalizující ukončení interaktivního režimu."""
    def __init__(self, message: Optional[str] = None):
        self.message = message
        super().__init__(self.message)
