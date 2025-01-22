from abc import ABC, abstractmethod
from typing import Optional, Any

class ExitInteractiveModeMixin(ABC):

    @staticmethod
    def _exit_interactive_mode(message: Optional[str] = None) -> None:
        """
        Ukončí interaktivní režim s volitelnou zprávou.

        Args:
            message (Optional[str]): Zpráva zobrazená před ukončením.
        """
        if message:
            print(f"\n{message}")
        print("Ukončuji interaktivní režim...")
