from typing import List
from ._get_simplified_traceback import get_simplified_traceback  # instance, ne funkce!
# POZOR: není to funkce, ale instance třídy SimplifiedTracebackCallable

class VerifyError(Exception):
    """Základní výjimka knihovny Verify, obsahuje kostru chybové zprávy."""

    # Třída by mohla mít i class-atributy jako defaultní nadpisy
    title: str = "\n⚠ DOŠLO K CHYBĚ PŘI OVĚŘOVÁNÍ!\n"
    what_happened_intro: str = "» Co se stalo:\n"
    what_to_do_intro: str = "» Jak to opravit:\n"

    def __init__(
            self,
            what_happened: List[str],
            what_to_do: List[str],
    ):
        """
        Inicializuje výjimku s předdefinovanou kostrou zprávy.

        Args:
            what_happened (List[str]): Popis chyby.
            what_to_do (List[str]): Doporučení k nápravě.
        """
        self.traceback = get_simplified_traceback()
        self.what_happened = what_happened
        self.what_to_do = what_to_do

        self.message = (
                ''.join(self.traceback) + "\n" +
                self.title +
                self.what_happened_intro +
                ''.join(self.what_happened) +
                self.what_to_do_intro +
                ''.join(self.what_to_do)
        )

        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
