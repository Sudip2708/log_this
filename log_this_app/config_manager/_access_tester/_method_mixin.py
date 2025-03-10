from abc import ABC

from abc_helper import abc_property


class ContentMismatchError(Exception):
    """Výjimka vyvolaná, pokud se obsah souboru neshoduje s očekáváním."""
    pass


class AccessTesterMethodsMixin(ABC):

    # Atribut pro cestu k testovacímu souboru
    _test_message = abc_property("_test_message")


    def _write_test(self):
        """Otestuje zápis souboru."""

        # Zaznamenání startu testu
        self._start_test = True

        # Vytvoření souboru
        with self._test_file.open("w") as f:
            f.write(self._test_message)

        # Zaznamenání úspěšného vytvoření souboru
        self._can_write = True


    def _read_test(self):
        """Otestuje čtení souboru."""

        # Čtení souboru
        with self._test_file.open("r") as f:
            if f.read() != self._test_message:
                self._content_mismatch = f.read()
                raise ContentMismatchError(
                    f"Načtený obsah: {self._test_message}, "
                    f"neodpovídá zapsanému: {self._content_mismatch}."
                )

        # Zaznamenání úspěšného čtení souboru
        self._can_read = True


    def _delete_test(self):
        """Otestujemazání souboru."""

        # Smazání souboru
        self._test_file.unlink()

        # Zaznamenání úspěšného smazání souboru
        self._can_delete = True


    def _attributes_reset(self):
        """Resetuje atributy na původní hodnoty"""

        self._content_mismatch = None
        self._start_test = False
        self._can_write = False
        self._can_read = False
        self._can_delete = False
        self._test_file = None


    def _final_test_evaluation(self):
        """Závěrečné upřesnění kde v testech došlo k chybě"""
        if not self._start_test:
            print("Test se zastavil v přípravné fázy a k testování přístupu nedošlo.")
        elif not self._can_write:
            print("Test se zastavil při vytváření testovacího dokumentu.")
        elif not self._can_read:
            print("Test se zastavil při čtení testovacího dokumentu.")
        elif not self._can_delete:
            print("Test se zastavil při mazání testovacího dokumentu.")


    def _final_test_file_clean_up(self):
        """Metoda pro závěrečné případné odstranění testovacího souboru"""

        # Kontrola zda soubor existuje
        if self._test_file and self._test_file.exists():

            try:
                # Smazání souboru
                self._test_file.unlink()

            except (OSError, PermissionError) as e:
                print("Po testu zůstal testovací soubor, který nelze smazat.")
                print(f"Cesta k souboru: {self._test_file}")
                print(f"Zachycené podrobnosti: {e}")
                print("Možné řešení: Zkontrolujte umístění a pokuste se soubor smazat ručně.")
