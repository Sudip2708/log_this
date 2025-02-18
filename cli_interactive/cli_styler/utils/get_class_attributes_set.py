from typing import Set, List


def get_class_attributes_set(class_attributes: List[str]) -> Set[str]:
    """
    Vrátí množinu atributů třídy odpovídajících stylům.

    :param class_attributes: Seznam atributů získaný z `dir(instance)`.
    :return: Množina názvů atributů odpovídajících stylům.

    :raises TypeError: Pokud vstup není seznam řetězců.
    """

    # Ověříme, že vstup je seznam
    if not isinstance(class_attributes, list):
        raise TypeError(f"Expected list, got {type(class_attributes).__name__}")

    # Ověříme, že seznam obsahuje pouze řetězce
    if not all(isinstance(attr, str) for attr in class_attributes):
        raise TypeError("Expected list of strings, but found other types.")

    # Filtrujeme jen relevantní atributy (bez speciálních metod `__xxx__`)
    return {
        key for key in class_attributes
        if not key.startswith("_")  # Odstraníme speciální atributy
           and key != "init"  # Ujistíme se, že `init` není součástí
    }
