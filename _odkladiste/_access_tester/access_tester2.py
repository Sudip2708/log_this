from pathlib import Path
import os

from cli_styler import cli_print


class AccessTester:

    _path = None
    _target_dir = None
    _test_file_path = None

    def __call__(self, path: Path):
        self._path = path
        return (
            True
            if self._is_path_instance()
               and self._is_correct_format()
               and self._is_dir_present()
               and self._can_save_file()
               and self._can_read_file()
               and self._can_delete_file()
            else False
        )

    # Ověření, zda path je instancí Path
    def _is_path_instance(self):
        if not isinstance(self._path, Path):
            cli_print.warning.text("Cesta není zadaná jako instance Path! ")
            cli_print.warning.text(f"Očekáván typ: {Path.__name__} ")
            cli_print.warning.text(f"Získáný typ: {type(self._path).__name__} ")
            cli_print.warning.text(f"Zadaná cesta: {self._path} ")
            return False

    # Ověření zda je správně uvedena cílová složka
    def _is_correct_format(self):
        self._target_dir = self._path if self._path.is_dir() else self._path.parent
        if not self._target_dir.is_dir():
            cli_print.warning.text("Není zadán správný formát cesty. ")
            cli_print.warning.text("Není správně definována koncová složka. ")
            cli_print.warning.text(f"Zadaná cesta: {self._path} ")
            return False

    # Ověření, zda koncová složka existuje
    def _is_dir_present(self):
        try:
            self._target_dir.mkdir(parents=True, exist_ok=True)
        except FileExistsError:
            cli_print.warning.text("Není zadán správný formát cesty. ")
            cli_print.warning.text("Některá z rodičovských složek je soubor. {self._target_dir} ")
            cli_print.warning.text(f"Zadaná cesta: {self._target_dir} ")
            return False
        except (FileNotFoundError, PermissionError):
            cli_print.warning.text("Nepovedlo se vytvořit cílovou složku. ")
            cli_print.warning.text(f"Pravděpodobně chybí dostatečná oprávnění. ")
            cli_print.warning.text(f"Zadaná cesta: {self._target_dir} ")
            return False
        except OSError as e:
            cli_print.warning.text("Nepovedlo se vytvořit cílovou složku. ")
            cli_print.warning.text(f"Vyskytla se chyba operačního systému. ")
            cli_print.warning.text(f"Popis chyby: {e} ")
            return False
        except Exception as e:
            cli_print.warning.text("Nepovedlo se vytvořit cílovou složku. ")
            cli_print.warning.text(f"Nastala neočekávaná chyba. ")
            cli_print.warning.text(f"Popis chyby: {e} ")
            return False

    # Test vytvoření souboru
    def _can_save_file(self):
        # Vytvoření cesty k testovacímu souboru
        self._test_file_path = self._target_dir / f"_test_file_{os.getpid()}.tmp"
        try:
            with self._test_file_path.open("w") as test_file:
                test_file.write("test_message")
        except PermissionError:
            cli_print.warning.text("Nepovedlo se vytvořit testovací soubor. ")
            cli_print.warning.text(f"Pravděpodobně chybí dostatečná oprávnění pro zápis/čtení. ")
            cli_print.warning.text(f"Testovaná cesta: {self._test_file_path} ")
            return False
        except OSError as e:
            cli_print.warning.text("Nepovedlo se vytvořit cílovou složku. ")
            cli_print.warning.text(f"Vyskytla se chyba operačního systému. ")
            cli_print.warning.text(f"Popis chyby: {e} ")
            return False
        except Exception as e:
            cli_print.warning.text("Nepovedlo se vytvořit cílovou složku. ")
            cli_print.warning.text(f"Nastala neočekávaná chyba. ")
            cli_print.warning.text(f"Popis chyby: {e} ")
            return False

    # Test čtení souboru
    def _can_read_file(self):
        try:
            with self._test_file_path.open("r") as test_file:
                content = test_file.read()
                if not content:
                    cli_print.warning.text("Vyskytla se chyba při čtení testovacího souboru. ")
                    cli_print.warning.text("Načtený obsah neobsahuje zapsaný text a je prázdný. ")
                    return False
                if content != "test_message":
                    cli_print.warning.text( "Vyskytla se chyba při čtení testovacího souboru. ")
                    cli_print.warning.text("Načtený obsah neodpovídá zapsanému obsahu. ")
                    return False
        except FileNotFoundError:
            cli_print.warning.text("Vyskytla se chyba při čtení testovacího souboru. ")
            cli_print.warning.text(f"Soubor po uložení nebyl nalezen: {self._test_file_path}")
            cli_print.warning.text(f"Cesta k souboru: {self._test_file_path} ")
            return False
        except PermissionError:
            cli_print.warning.text("Vyskytla se chyba při čtení testovacího souboru. ")
            cli_print.warning.text(f"Pravděpodobně chybí dostatečná oprávnění pro zápis/čtení. ")
            cli_print.warning.text(f"Cesta k souboru: {self._test_file_path} ")
            return False
        except OSError as e:
            cli_print.warning.text("Vyskytla se chyba při čtení testovacího souboru. ")
            cli_print.warning.text("Vyskytla se chyba operačního systému. ")
            cli_print.warning.text(f"Popis chyby: {e} ")
            return False
        except Exception as e:
            cli_print.warning.text("Vyskytla se chyba při čtení testovacího souboru. ")
            cli_print.warning.text("Nastala neočekávaná chyba. ")
            cli_print.warning.text(f"Popis chyby: {e} ")
            return False


    def _can_delete_file(self):
        try:
            if self._test_file_path.exists():
                self._test_file_path.unlink()
        except OSError as e:
            cli_print.warning.text("Vyskytla se chyba při smazání testovacího souboru. ")
            cli_print.warning.text("Soubor se nepodařilo odstranit. ")
            cli_print.warning.text(f"Popis chyby: {e} ")
            return False
        except Exception as e:
            cli_print.warning.text("Vyskytla se chyba při čtení testovacího souboru. ")
            cli_print.warning.text("Nastala neočekávaná chyba. ")
            cli_print.warning.text(f"Popis chyby: {e} ")
            return False

