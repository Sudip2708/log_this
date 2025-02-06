from typing import Union

class ValueIsNotValid(Exception):
    """Výjimka signalizující uzadání hodnoty která je již zadaná."""
    def __init__(self, key: str, value: Union[str, int, bool]):
        self.message = (
            f"Neplatná hodnota '{value}' pro klíč '{key}'. \n"
            f"Žádná změna nebyla učiněna. \n"
        )
        super().__init__(self.message)