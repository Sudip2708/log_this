from .capture_logs import capture_logs
from .mock_function import mock_function
from .complex_object import complex_object

__all__ = [
    "capture_logs",  # Fixture pro zachycení log výstupů.
    "mock_function",  # Fixture pro vytvoření jednoduché mock funkce pro testování logování.
    "complex_object",  # Fixture pro vytvoření komplexního objektu pro testování serializace.
]
