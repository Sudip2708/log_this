from .._base_type_validator import BaseTypeValidator
import pathlib


class PathValidator(BaseTypeValidator):
    """
    Validátor pro pathlib.Path

    Hint:
        pathlib.Path = Objekt reprezentující cestu k souboru nebo adresáři
    """

    VALIDATOR_KEY = "Path"
    ANNOTATION = "pathlib.Path"
    INFO = "Definuje objekt reprezentující cestu k souboru nebo adresáři"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, pathlib.Path):
            raise TypeError(f"Hodnota '{value}' není validní pathlib.Path objekt.")
        return True