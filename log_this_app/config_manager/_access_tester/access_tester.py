from pathlib import Path
import os

from ._exception_handlers import *
from ._method_mixin import AccessTesterMethodsMixin, ContentMismatchError

class AccessTester(AccessTesterMethodsMixin):
    """Třída pro otestování práce se souborem s přidanou diagnostikou chyb"""

    _test_message = "This is a test message."
    _content_mismatch = None
    _start_test = False
    _can_write = False
    _can_read = False
    _can_delete = False

    def __call__(self, path: Path):

        try:
            # Ověření vstupu
            if not isinstance(path, Path):
                raise TypeError(f"Zadaná cesta: {path}, není instancí třídy Path.")

            # Vytvoření cesty k pro testovací soubor
            dir_path = path if path.is_dir() else path.parent
            self._test_file = dir_path / f"_test_file_{os.getpid()}.tmp"

            # Test zápisu, čtení a mazání
            self._write_test()
            self._read_test()
            self._delete_test()

            # Pokud vše proběhne v pořádku
            # print("Ověření zadané cesty proběhlo v pořádku.")
            return True

        # Chyba atributů instance třídy AccessTester.
        except AttributeError as e:
            attribute_error_handler(e)
            return False

        # Chyba v typu souboru (pokud by self._test_file nebyl instancí Path)
        except TypeError as e:
            type_error_handler(e)
            return False

        # Chyba v definici cesty k souboru
        except FileNotFoundError as e:
            file_not_found_error_handler(e)
            return False

        # Chyba v definici koncové složky
        except NotADirectoryError as e:
            not_a_directory_error_handler(e)
            return False

        # Nedostatečná oprávnění pro zápis
        except PermissionError as e:
            permission_error_handler(e)
            return False

        # Chyba při operacemi se souborem
        except OSError as e:
            os_error_handler(e)
            return False

        # Zachycení situace, kdy načtený obsah při testu neodpovídá uloženému
        except ContentMismatchError as e:
            content_mismatch_error_handler(e)
            return False

        # Zachycení neočekávaných chyb
        except Exception as e:
            exception_error_handler(e)
            return False

        finally:

            # Poznámka k diagnostice místa přeručení testu
            self._final_test_evaluation()

            # Reset atributů
            self._attributes_reset()

            # Kontrola, zda nezůstal po testu testovací soubor
            self._final_test_file_clean_up()


path_access_tester = AccessTester()