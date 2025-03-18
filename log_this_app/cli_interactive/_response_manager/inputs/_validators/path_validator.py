from prompt_toolkit.validation import Validator, ValidationError
from pathlib import Path


class PathValidator(Validator):
    """
    Univerzální validátor pro cesty k souborům nebo složkám.
    Možnost validovat existenci a ověřovat příponu souboru.
    """

    def __init__(self, check_folder_only=False, must_be_json=False):
        self.check_folder_only = check_folder_only
        self.must_be_json = must_be_json

    def validate(self, document):

        # Získání zadaného textu
        text = document.text.strip()

        if text:

            # Kontrola neplatných znaků
            if any(char in text for char in r'<>:"/\|?*'):
                raise ValidationError(message="Cesta obsahuje nepovolené znaky.")

            # Převod na instanci Path
            path = Path(text)

            # Kontrola absolutní cesty
            if not path.is_absolute():
                raise ValidationError(message="Cesta musí být absolutní.")

            # Kontrola existence zadané cesty
            if self.check_folder_only:
                dir_path = path if path.is_dir() else path.parent
                if not dir_path.exists():
                    raise ValidationError(message="Zadaná poslední složka neexistuje.")
            elif not path.exists():
                raise ValidationError(message="Zadaná cesta neexistuje.")

            # Kontrola souboru, zda je json
            if self.must_be_json and path.suffix.lower() != ".json":
                raise ValidationError(message="Soubor musí mít příponu .json")
