from pathlib import Path
import os

from cli_styler import cli_print


class AccessTester:
    """
    Testuje, zda je možné zapisovat a číst soubory na zadané cestě.
    Místo sekvenčního testování každého kroku používá přístup založený na
    jediném zkušebním procesu s detailním zachytáváním výjimek.
    """

    def __call__(self, path):
        """
        Provede test přístupu na zadané cestě.

        Args:
            path: Cesta k testování (Path nebo cokoliv konvertovatelné na Path)

        Returns:
            bool: True pokud test proběhl úspěšně, jinak False
        """
        try:
            # Pokus o převod na Path, pokud již není
            if not isinstance(path, Path):
                cli_print.warning.text("Cesta není zadaná jako instance Path!")
                cli_print.warning.text(f"Očekáván typ: {Path.__name__}")
                cli_print.warning.text(f"Získaný typ: {type(path).__name__}")
                cli_print.warning.text(f"Zadaná cesta: {path}")
                path = Path(path)

            # Zjištění cílové složky
            target_dir = path if path.is_dir() else path.parent

            # Pokus o vytvoření složky, čtení a zápis v jediném procesu
            return self._test_file_operations(target_dir)

        except TypeError:
            cli_print.warning.text("Cesta nemůže být převedena na typ Path.")
            cli_print.warning.text(f"Zadaná cesta: {path}")
            return False
        except Exception as e:
            cli_print.warning.text(
                f"Neočekávaná chyba při testování přístupu: {e}")
            return False

    def _test_file_operations(self, target_dir):
        """
        Provede kompletní test operací se soubory v jedné metodě.
        """
        test_file_path = None

        try:
            # 1. Test existence nebo vytvoření složky
            try:
                target_dir.mkdir(parents=True, exist_ok=True)
            except FileExistsError:
                cli_print.warning.text("Není zadán správný formát cesty.")
                cli_print.warning.text(
                    f"Některá z rodičovských složek je soubor: {target_dir}")
                return False
            except PermissionError:
                cli_print.warning.text("Nepovedlo se vytvořit cílovou složku.")
                cli_print.warning.text(
                    "Pravděpodobně chybí dostatečná oprávnění.")
                cli_print.warning.text(f"Zadaná cesta: {target_dir}")
                return False

            # 2. Vytvoření testovacího souboru
            test_file_path = target_dir / f"_test_file_{os.getpid()}.tmp"
            with test_file_path.open("w") as test_file:
                test_file.write("test_message")

            # 3. Test čtení souboru
            with test_file_path.open("r") as test_file:
                content = test_file.read()
                if content != "test_message":
                    cli_print.warning.text(
                        "Vyskytla se chyba při čtení testovacího souboru.")
                    cli_print.warning.text(
                        "Načtený obsah neodpovídá zapsanému obsahu.")
                    return False

            # 4. Smazání testovacího souboru
            test_file_path.unlink()

            # Pokud vše proběhlo bez chyby, vrátíme True
            return True

        except FileNotFoundError:
            cli_print.warning.text(
                "Vyskytla se chyba při přístupu k souboru nebo složce.")
            cli_print.warning.text(
                f"Cesta nebyla nalezena: {test_file_path or target_dir}")
            return False
        except PermissionError:
            cli_print.warning.text("Nepovedlo se provést operaci se souborem.")
            cli_print.warning.text(
                "Pravděpodobně chybí dostatečná oprávnění pro zápis/čtení.")
            cli_print.warning.text(
                f"Testovaná cesta: {test_file_path or target_dir}")
            return False
        except OSError as e:
            cli_print.warning.text("Nepovedlo se provést operaci se souborem.")
            cli_print.warning.text("Vyskytla se chyba operačního systému.")
            cli_print.warning.text(f"Popis chyby: {e}")
            return False
        except Exception as e:
            cli_print.warning.text("Nepovedlo se provést operaci se souborem.")
            cli_print.warning.text(f"Nastala neočekávaná chyba: {e}")
            return False
        finally:
            # Úklid: odstranění testovacího souboru, pokud existuje
            if test_file_path and test_file_path.exists():
                try:
                    test_file_path.unlink()
                except Exception:
                    pass  # Ignorujeme chyby při úklidu