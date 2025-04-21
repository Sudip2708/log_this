import os
from pathlib import Path
from typing import Union, Sequence


from ._exceptions import InvalidPathInputError, VerifyUnexpectedError


# Typové aliasy
PathLike = Union[str, Path]
PathLikeSequence = Sequence[PathLike]


# Definice funkce
def normalize_paths(
        input_paths: Union[PathLike, PathLikeSequence]
) -> list[str]:
    """
    Převede jeden nebo více vstupních cest na seznam absolutních cest ve formátu string.

    Argument může být:
    - řetězec cesty (`str`)
    - objekt `Path`
    - sekvence těchto typů (např. `list[str]`, `tuple[Path]`, `set[str | Path]`)

    Výsledkem je vždy seznam normalizovaných cest (`list[str]`), připravených k porovnávání
    nebo použití např. v ignorovacím mechanismu.

    Args:
        input_paths: Jedna nebo více cest k převedení.

    Returns:
        Seznam absolutních cest jako řetězců.

    Raises:
        InvalidPathInputError: Pokud vstup obsahuje nepovolený typ.
        VerifyUnexpectedError: Pokud dojde k neočekávané chybě.

    Příklady použití:

        # Jeden řetězec
        print("1:", normalize_paths("~"))

        # Objekt Path
        print("2:", normalize_paths(Path(".")))

        # Seznam cest
        print("3:", normalize_paths(["/usr", Path("/etc")]))

        # Set cest
        print("4:", normalize_paths({"/tmp", Path("/var/log")}))

        # Neplatný vstup
        print("5:", normalize_paths(123))

    """
    try:

        # Převod samostatně zadané cesty na seznam.
        if isinstance(input_paths, (str, Path)):
            input_paths = [input_paths]

        # Kontrola povolených kontejnerů
        elif not isinstance(input_paths, (list, tuple, set)) or not input_paths:
            raise InvalidPathInputError(
                f"Očekávána cesta nebo sekvence cest typu str nebo Path, "
                f"obdrženo: {type(input_paths)}"
            )

        # Seznam pro ověřené a normalizované cesty
        normalized = []

        # Cyklus prochzející jednotlivé cesty
        for item in input_paths:

            # Kontrola zda je cesta str a nebo path
            if not isinstance(item, (str, Path)):
                raise InvalidPathInputError(
                    f"Zadaná cesta neprošla validací!"
                    f"Vstup obsahuje nepodporovaný typ: {type(item)}"
                )

            # Normalizování cesty a přidání do seznamu
            # os.fspath dává jistotu konverze Path na str
            normalized.append(os.path.abspath(os.fspath(item)))

        # Návrácení seznamu s ověřenými a normalizovanými cestami
        return list(map(str, normalized))

    # Propagace interních víjimek
    except InvalidPathInputError:
        raise

    # Ošetření případů, kdy by samotná funkce způsobila chybu
    except Exception as e:
        raise VerifyUnexpectedError(
            f"Neočekávaná chyba zachycená ve funkci 'normalize_paths' "
            f"určené pro převod vstupních cest na seznam absolutních cest."
            f"Záznam o chybě: {e}"
        ) from e



# Testy
import unittest

class TestNormalizePaths(unittest.TestCase):
    """
    Kompletní sada testů pro funkci `normalize_paths`

    - pomocí standardního modulu `unittest`
    - se zohledněním:
      - správných vstupů (`str`, `Path`, kombinace, sekvence)
      - špatných typů (např. `int`, `dict`)
      - vnořených chyb
      - ošetření výjimek


    Spuštění testů: python -m unittest test_normalize_paths.py


    | Test | Co ověřuje |
    |------|------------|
    | `test_single_str_path` | jeden string |
    | `test_single_path_object` | jeden Path objekt |
    | `test_list_of_str_paths` | list stringů |
    | `test_list_of_path_objects` | list `Path` objektů |
    | `test_mixed_types` | kombinovaný vstup |
    | `test_tuple_and_set_input` | tuple a set vstup |
    | `test_invalid_single_type` | nesprávný typ jako vstup |
    | `test_invalid_in_sequence` | chyba uvnitř sekvence |
    | `test_unexpected_error_wrapped` | vnořená chyba uvnitř `os.path.abspath` |

    """

    def setUp(self):
        # Příprava referenčních cest
        self.cwd = os.path.abspath(".")
        self.home = os.path.abspath(str(Path.home()))

    def test_single_str_path(self):
        result = normalize_paths(".")
        self.assertEqual(result, [self.cwd])

    def test_single_path_object(self):
        result = normalize_paths(Path("."))
        self.assertEqual(result, [self.cwd])

    def test_list_of_str_paths(self):
        input_paths = [".", str(Path.home())]
        expected = [self.cwd, self.home]
        self.assertEqual(normalize_paths(input_paths), expected)

    def test_list_of_path_objects(self):
        input_paths = [Path("."), Path.home()]
        expected = [self.cwd, self.home]
        self.assertEqual(normalize_paths(input_paths), expected)

    def test_mixed_types(self):
        input_paths = [".", Path.home()]
        expected = [self.cwd, self.home]
        self.assertEqual(normalize_paths(input_paths), expected)

    def test_tuple_and_set_input(self):
        self.assertEqual(
            set(normalize_paths((".", Path.home()))),
            set([self.cwd, self.home])
        )
        self.assertEqual(
            set(normalize_paths({".", Path.home()})),
            set([self.cwd, self.home])
        )

    def test_invalid_single_type(self):
        with self.assertRaises(InvalidPathInputError):
            normalize_paths(123)

    def test_invalid_in_sequence(self):
        with self.assertRaises(InvalidPathInputError):
            normalize_paths([".", 123])

    def test_unexpected_error_wrapped(self):
        # Simulace selhání přes mockovaný os.path.abspath
        from unittest.mock import patch

        with patch("os.path.abspath", side_effect=ValueError("Něco se pokazilo")):
            with self.assertRaises(VerifyUnexpectedError) as cm:
                normalize_paths(".")

            self.assertIn("Neočekávaná chyba", str(cm.exception))

    def test_empty_input_raises_error(self):
        with self.assertRaises(InvalidPathInputError):
            normalize_paths([])


# Lokální zpuštění testů
if __name__ == "__main__":
    unittest.main()


