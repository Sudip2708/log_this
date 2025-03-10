from pathlib import Path
import os
import shutil

class ContentMismatchError(Exception):
    """Výjimka vyvolaná, pokud se obsah souboru neshoduje s očekáváním."""
    pass

from .exceptions_handlers import *

class AccessTester:
    """Třída pro otestování práce se souborem s přidanou diagnostikou chyb"""

    _test_message = "This is a test."
    _content_mismatch = None
    _start_test = False
    _can_write = False
    _can_read = False
    _can_delete = False

    def __call__(self, path: Path) -> bool:

        try:
            # Ověření vstupu
            if not isinstance(path, Path):
                raise TypeError("Zadaná cesta není instancí třídy Path.")

            # Vytvoření cesty k pro testovací soubor
            dir_path = path if path.is_dir() else path.parent
            self._test_file = dir_path / f"_test_file_{os.getpid()}.tmp"

            # Test zápisu, čtení a mazání
            self._write_test()
            self._read_test()
            self._delete_test()

            # Pokud vše proběhne v pořádku
            print("Ověření zadané cesty proběhlo v pořádku.")
            return True

        # Chyba atributů instance třídy AccessTester.
        except AttributeError as e:
            attribute_error_handler(e)

        # Chyba v typu souboru (pokud by self._test_file nebyl instancí Path)
        except TypeError as e:
            type_error_handler(e)

        # Chyba v definici cesty k souboru
        except FileNotFoundError as e:
            file_not_found_error_handler(e)

        # Chyba v definici koncové složky
        except NotADirectoryError as e:
            not_a_directory_error_handler(e)

        # Nedostatečná oprávnění pro zápis
        except PermissionError as e:
            permission_error_handler(e)

        # Chyba při operacemi se souborem
        except OSError as e:
            os_error_handler(e)

        # Zachycení situace, kdy načtený obsah při testu neodpovídá uloženému
        except ContentMismatchError as e:
            content_mismatch_error_handler(e)

        finally:

            # Poznámka k diagnostice místa přeručení testu
            self._final_test_evaluation()

            # Kontrola, zda nezůstal po testu testovací soubor
            self._final_test_file_clean_up()

            # Reset atributů
            self._attributes_reset()

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

    def _final_test_file_clean_up(self):
        """Metoda pro závěrečné případné odstranění testovacího souboru"""
        if self._test_file.exists():
            try:
                self._test_file.unlink()
            except Exception:
                print("Po testu cesty zbyl testovací soubor, který nelze smazat.")
                print(f"Cesta k souboru: {self._test_file}")
                print("Možné řešení: Zkontrolujte umístění a pokuste se soubor smazt ručně.")

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