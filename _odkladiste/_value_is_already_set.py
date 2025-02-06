from typing import Union

class ValueIsAlreadySet(Exception):
    """Výjimka signalizující uzadání hodnoty která je již zadaná."""
    def __init__(self, key: str, value: Union[str, int, bool]):
        self.message = (
            f"The configuration key '{key}' is already set to '{value}'. \n"
            f"Žádná změna nebyla učiněna. \n"
        )
        super().__init__(self.message)