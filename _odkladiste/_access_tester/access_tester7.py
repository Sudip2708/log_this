from pathlib import Path
import os
import shutil


class AccessTester:
    def __call__(self, path: str) -> bool:
        print("\n=== Spuštění diagnostiky přístupu ===")

        # 1️⃣ Ověření formátu cesty
        if not self.is_valid_path(path):
            return False

        # 2️⃣ Ověření oprávnění k zápisu
        if not self.has_write_permission(path):
            return False

        # 3️⃣ Kontrola možných systémových omezení
        if not self.check_os_restrictions(path):
            return False

        # 4️⃣ Pokus o vytvoření složky / podsložky
        if not self.test_create_directory(path):
            return False

        # 5️⃣ Test zápisu, čtení a mazání souboru
        if not self.test_file_operations(path):
            return False

        print("\n✅ Diagnostika proběhla úspěšně – přístup je v pořádku!")
        return True

    def is_valid_path(self, path: str) -> bool:
        """Ověří správnost formátu cesty."""
        print("\nKontrola správnosti cesty...")
        path_obj = Path(path)

        if not path_obj.is_absolute():
            print("- Cesta není absolutní.")
            return False

        if any(char in '*?"<>|' for char in path):
            print("- Cesta obsahuje neplatné znaky.")
            return False

        if len(path) > 255:
            print("- Cesta je příliš dlouhá.")
            return False

        if not path_obj.parent.exists():
            print("- Rodičovská složka neexistuje.")
            return False

        print("- Cesta je validní.")
        return True

    def has_write_permission(self, directory: str) -> bool:
        """Ověří oprávnění k zápisu."""
        print("\nKontrola oprávnění pomocí os.access()")

        if os.access(directory, os.W_OK):
            print("- Oprávnění k zápisu v pořádku.")
            return True

        print("- Nedostatečná oprávnění k zápisu!")
        return False

    def check_os_restrictions(self, directory: str) -> bool:
        """Ověří možné systémové překážky pro vytvoření souboru."""
        print("\nKontrola možných OSError scénářů...")

        total, used, free = shutil.disk_usage(directory)
        if free < 1024 * 1024:
            print("- Nedostatek volného místa na disku.")
            return False

        if os.path.ismount(directory):
            print("- Cesta ukazuje na síťový nebo odpojený disk.")
            return False

        return True

    def test_create_directory(self, directory: str) -> bool:
        """Otestuje možnost vytvoření složky nebo podsložky."""
        print("\nTestování možnosti vytvoření složky...")
        path = Path(directory)

        if not path.exists():
            try:
                path.mkdir(parents=True, exist_ok=True)
                print("- Hlavní složka vytvořena.")
                return True
            except OSError as e:
                print(f"- Chyba při vytváření složky: {e}")
                return False

        test_subdir = path / "_test_dir_tmp"
        try:
            test_subdir.mkdir()
            test_subdir.rmdir()
            print("- Testovací podsložka úspěšně vytvořena a smazána.")
            return True
        except OSError as e:
            print(f"- Chyba při manipulaci s testovací složkou: {e}")
            return False

    def test_file_operations(self, directory: str) -> bool:
        """Otestuje zápis, čtení a mazání souboru."""
        print("\nTestování práce se souborem...")
        test_file = Path(directory) / "_test_file_tmp.txt"

        try:
            with test_file.open("w") as f:
                f.write("test_message")
            print("- Soubor úspěšně vytvořen a zapsán.")

            with test_file.open("r") as f:
                if f.read() != "test_message":
                    print("- Obsah souboru neodpovídá očekávání!")
                    return False
            print("- Čtení souboru proběhlo úspěšně.")

            test_file.unlink()
            print("- Soubor úspěšně smazán.")
            return True

        except OSError as e:
            print(f"- Chyba při manipulaci se souborem: {e}")
            return False
