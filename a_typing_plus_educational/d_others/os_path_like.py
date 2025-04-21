from .._base_type_validator import BaseTypeValidator
import os


class PathLikeValidator(BaseTypeValidator):
    """
    Validátor pro os.PathLike

    Hint:
        os.PathLike = Objekt konvertovatelný na cestu, implementující __fspath__
    """

    VALIDATOR_KEY = "PathLike"
    ANNOTATION = "os.PathLike"
    INFO = "Definuje objekt konvertovatelný na cestu"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not hasattr(value, "__fspath__"):
            raise TypeError(f"Hodnota '{value}' není validní os.PathLike objekt.")
        return True