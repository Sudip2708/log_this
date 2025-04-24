import inspect

from ._verify_error import VerifyError


class InternalUnexpectedError(VerifyError):
    """Výjimka vyvolaná při neočekávané události."""

    title = "\n⚠ DOŠLO K NEOČEKÁVANÉ INTERNÍ CHYBĚ!\n"
    function = '<neznámá funkce>'
    module = '<neznámý modul>'

    def __init__(
        self,
        original_exception: Exception,

    ):
        # Načtení atributů
        self.exc = original_exception
        self.get_function_and_module()

        # Popis toho co se stalo
        what_happened = [
            f"   - Výjimku vyvolal: {self.function}() z {self.module}\n"
            f"   - Zachycená výjimka: {type(self.exc).__name__} - {str(self.exc)}.\n"
        ]

        # Popis toho co se dá dělat
        what_to_do = [
            "   - Tato situace by za běžných okolností neměla nastat a pravděpodobně značí chybu v kódu.\n",
            "   - Zkontroluj vývojářskou logiku nebo prosím nahlas chybu s podrobným popisem.\n",
        ]

        # Volání nadřazené výjimky pro zpracování výstupu
        super().__init__(what_happened, what_to_do)


    def get_function_and_module(self):
        """
        Načte název funkce a modulu, ve kterých byla tato výjimka vyvolána.

        Metoda použije zásobník volání k identifikaci místa, odkud byla výjimka
        `InternalUnexpectedError` inicializována. To umožní přesněji popsat kontext
        chyby a pomáhá při ladění.
        """

        # Načtení aktuálního rámce zásobníku
        current_frame = inspect.currentframe()

        # Získání okolních rámců (včetně volajícího)
        outer_frames = (
            inspect.getouterframes(current_frame, 2)
            if current_frame else []
        )

        # Výběr rámce volající funkce (1 úroveň nad tímto kódem)
        outer_frame = (
            outer_frames[1]
            if len(outer_frames) > 1 else None
        )

        # Pokud byl rámec úspěšně získán
        if outer_frame:

            # Ulož jméno volající funkce
            self.function = outer_frame.function

            # Pokud existuje odkaz na rámec (kvůli globálním proměnným)
            if outer_frame.frame:
                # Ulož název modulu (nebo ponech výchozí, pokud nelze zjistit)
                self.module = outer_frame.frame.f_globals.get(
                    '__name__', self.module
                )



