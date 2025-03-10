from pathlib import Path
import os
from cli_styler import cli_print


class AccessTester:
    def __call__(self, path: Path) -> bool:
        try:
            self._validate_path(path)
            self._validate_directory()
            self._test_file_operations()
            return True
        except (InvalidPathError, PermissionError, OSError) as e:
            cli_print.warning.text(f"Chyba přístupu k souboru: {e}")
            return False

    def _validate_path(self, path: Path):
        if not isinstance(path, Path):
            raise InvalidPathError(f"Cesta není instance Path: {type(path).__name__}")
        self._path = path
        self._target_dir = path if path.is_dir() else path.parent

    def _validate_directory(self):
        if not self._target_dir.is_dir():
            raise InvalidPathError(f"Cílová složka neexistuje: {self._target_dir}")
        try:
            self._target_dir.mkdir(parents=True, exist_ok=True)
        except FileExistsError:
            raise InvalidPathError(f"Rodičovská složka je soubor: {self._target_dir}")
        except PermissionError:
            raise PermissionError(f"Nedostatečná oprávnění pro: {self._target_dir}")

    def _test_file_operations(self):
        test_file = self._target_dir / f"_test_file_{os.getpid()}.tmp"
        try:
            with test_file.open("w") as f:
                f.write("test_message")
            with test_file.open("r") as f:
                content = f.read()
                if content != "test_message":
                    raise OSError("Čtení souboru se neshoduje se zápisem.")
        finally:
            if test_file.exists():
                test_file.unlink()


class InvalidPathError(Exception):
    """Výjimka pro neplatnou cestu."""
