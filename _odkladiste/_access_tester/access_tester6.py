from pathlib import Path
import os

from cli_styler import cli_print
from pathlib import Path
import os
import string
import shutil
# class AccessTester:


def is_valid_path(path: str) -> bool:
    """Ověří, zda je zadaná cesta správně formátovaná a může existovat."""
    print("Kontrola správnosti cesty...")

    path_obj = Path(path)

    # Ověření, zda je cesta absolutní
    if not path_obj.is_absolute():
        print("- Cesta není absolutní.")
        print("- Možné příčiny: Relativní cesty mohou být chybně interpretovány.")
        print("- Návrh řešení: Použijte absolutní cestu (např. `/home/user/folder`).")
        return False

    # Ověření neplatných znaků (pro Windows i Unix)
    invalid_chars = set('*?"<>|')  # Windows nepovoluje tyto znaky
    if any(char in invalid_chars for char in path):
        print("- Cesta obsahuje neplatné znaky.")
        print(f"- Zakázané znaky: {' '.join(invalid_chars)}")
        print("- Návrh řešení: Odeberte zakázané znaky ze jména souboru/složky.")
        return False

    # Ověření maximální délky cesty
    if len(path) > 255:
        print("- Cesta je příliš dlouhá.")
        print("- Možné příčiny: Některé systémy omezují délku cesty na 255 znaků.")
        print("- Návrh řešení: Zkraťte název složek nebo souboru.")
        return False

    # Ověření, zda rodičovská složka existuje
    if not path_obj.parent.exists():
        print("- Rodičovská složka neexistuje.")
        print("- Možné příčiny: Cesta obsahuje neexistující adresář.")
        print("- Návrh řešení: Ověřte, zda jsou všechny složky v cestě vytvořené.")
        return False

    print("- Cesta je validní.")
    return True

def has_write_permission1(directory: str) -> bool:
    """Zkontroluje pomocí os.access(), zda je možné zapisovat do složky."""
    print("Kontrola oprávnění pomocí os.access()")
    if os.access(directory, os.W_OK)
        print("- Vše v pořádku")
    else:
        print("- Kontrola zjistila nedostatečné oprávnění pro zápis na dané umístění")
        print("- Možné příčiny: ")
        print("- Návrh řešení: ")

import os

def has_write_permission2(directory: str) -> bool:
    """Zkontroluje pomocí os.access(), zda je možné zapisovat do složky."""
    print("Kontrola oprávnění pomocí os.access()")

    if os.access(directory, os.W_OK):
        print("- Vše v pořádku, oprávnění k zápisu je uděleno.")
        return True

    print("- Kontrola zjistila nedostatečné oprávnění pro zápis na dané umístění.")
    print("- Možné příčiny:")
    print("  1️⃣ Nemáte dostatečná oprávnění k zápisu do této složky.")
    print("  2️⃣ Složka patří jinému uživateli nebo skupině.")
    print("  3️⃣ Složka je jen pro čtení (např. součást systémového adresáře).")
    print("  4️⃣ Oprávnění mohla být změněna administrátorem (např. pomocí ACL).")
    print("  5️⃣ Souborový systém nebo disk je v režimu jen pro čtení.")

    print("- Návrh řešení:")
    print("  ✅ Ověřte oprávnění pomocí příkazu `ls -ld <cesta>` (Linux/macOS) nebo `icacls <cesta>` (Windows).")
    print("  ✅ Zkuste složku vlastnit (`chown <uživatel> <cesta>` na Linuxu).")
    print("  ✅ Zkuste změnit oprávnění (`chmod u+w <cesta>` na Linuxu).")
    print("  ✅ Na Windows klikněte pravým tlačítkem na složku → Vlastnosti → Zabezpečení.")
    print("  ✅ Pokud je disk jen pro čtení, zkuste jej připojit s oprávněním pro zápis.")

    return False

def check_os_restrictions(directory: str) -> bool:
    """Diagnostika možných problémů způsobujících OSError před vytvořením složky."""
    print("Kontrola možných OSError scénářů...")

    # 1️⃣ Ověření volného místa na disku
    total, used, free = shutil.disk_usage(directory)
    if free < 1024 * 1024:  # Méně než 1 MB volného místa
        print("- Nedostatek volného místa na disku.")
        print("- Možné příčiny: Disk je plný nebo má systém omezení.")
        print("- Návrh řešení: Uvolněte místo na disku.")
        return False

    # 2️⃣ Ověření, zda je cesta síťový disk nebo připojené zařízení
    if os.path.ismount(directory):
        print("- Cesta ukazuje na připojený disk nebo síťový svazek.")
        print("- Možné příčiny: Síťový disk může být odpojen nebo nemá oprávnění.")
        print("- Návrh řešení: Ověřte připojení a oprávnění svazku.")
        return False

    # 3️⃣ Ověření, zda ve složce není extrémně mnoho souborů (může zpomalit FS)
    try:
        if len(os.listdir(directory)) > 100000:  # Např. 100 000 souborů ve složce
            print("- Složka obsahuje extrémně mnoho souborů.")
            print("- Možné příčiny: Omezení souborového systému.")
            print("- Návrh řešení: Zkuste vytvořit složku jinde nebo vyčistit adresář.")
            return False
    except PermissionError:
        print("- Nemáme práva číst obsah složky.")
        print("- Možné příčiny: Oprávnění nebo šifrovaná složka.")
        print("- Návrh řešení: Zkuste spustit jako administrátor.")
        return False

    print("- Nezjistili jsme žádné zjevné problémy, můžeme pokračovat.")
    return True


def test_create_directory(directory: str) -> bool:
    """Otestuje, zda lze vytvořit složku nebo testovací podsložku."""
    print("Testování možnosti vytvoření složky...")

    path = Path(directory)

    # 1️⃣ Pokus o vytvoření hlavní složky, pokud neexistuje
    if not path.exists():
        try:
            path.mkdir(parents=True, exist_ok=True)
            print("- Hlavní složka byla úspěšně vytvořena.")
            return True
        except OSError as e:
            print("- Selhalo vytvoření hlavní složky!")
            print(f"- Možné příčiny: {e}")
            print("- Návrh řešení: Ověřte oprávnění a volné místo na disku.")
            return False

    # 2️⃣ Pokud složka existuje, vytvoříme v ní testovací složku
    test_subdir = path / "_test_dir_tmp"
    try:
        test_subdir.mkdir()
        print("- Testovací podsložka úspěšně vytvořena.")

        # 3️⃣ Smazání testovací složky
        test_subdir.rmdir()
        print("- Testovací podsložka úspěšně smazána.")
        return True

    except OSError as e:
        print("- Selhalo vytvoření testovací podsložky!")
        print(f"- Možné příčiny: {e}")
        print("- Návrh řešení: Ověřte oprávnění a systémové limity.")
        return False


from pathlib import Path

def test_file_operations(directory: str) -> bool:
    """Otestuje vytvoření, zápis, čtení a mazání souboru v zadané složce."""
    print("Testování práce se souborem...")

    test_file = Path(directory) / "_test_file_tmp.txt"

    try:
        # 1️⃣ Pokus o vytvoření a zápis do souboru
        with test_file.open("w") as f:
            f.write("test_message")
        print("- Soubor byl úspěšně vytvořen a zapsán.")

        # 2️⃣ Pokus o čtení souboru
        with test_file.open("r") as f:
            content = f.read()
            if content != "test_message":
                print("- Chyba: Obsah souboru se neshoduje s očekáváním!")
                return False
        print("- Čtení souboru proběhlo úspěšně.")

        # 3️⃣ Pokus o smazání souboru
        test_file.unlink()
        print("- Soubor byl úspěšně smazán.")

        return True

    except OSError as e:
        print("- Chyba při manipulaci se souborem!")
        print(f"- Možné příčiny: {e}")
        print("- Návrh řešení: Ověřte oprávnění a volné místo na disku.")
        return False
