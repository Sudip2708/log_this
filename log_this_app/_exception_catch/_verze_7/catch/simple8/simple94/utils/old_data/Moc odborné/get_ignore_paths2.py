import os
import site

from ._exceptions import InvalidPathInputError, VerifyUnexpectedError


def get_ignore_paths() -> list[str]:
    """
    Vrací seznam absolutních cest, které mají být ignorovány při určování 'uživatelského kódu'.

    Returns:
        list[str]: Seznam absolutních cest jako řetězce.

    Raises:
        VerifyUnexpectedError: Pokud dojde k neočekávané chybě během výpočtu.
    """

    try:

        # Definice základních systémových cest
        return [
            os.path.abspath(os.path.dirname(os.__file__)),
            *map(os.path.abspath, site.getsitepackages()),
            os.path.abspath(site.getusersitepackages())
        ]

    # Ošetření případů, kdy by samotná funkce způsobila chybu
    except Exception as e:
        raise VerifyUnexpectedError(
            f"Neočekávaná chyba zachycená ve funkci 'get_ignore_paths' "
            f"při generování ignorovaných cest: {e}"
        )



# Testy
import unittest
from unittest.mock import patch

class TestGetIgnorePaths(unittest.TestCase):

    @patch("os.path.abspath")
    @patch("site.getsitepackages")
    @patch("site.getusersitepackages")
    def test_default_behavior(self, mock_getusersitepackages,
                              mock_getsitepackages, mock_abspath):
        # Nastavíme, aby abspath vracel svůj argument (už předpokládáme absolutní cesty)
        mock_abspath.side_effect = lambda path: path
        mock_getsitepackages.return_value = ["/fake/site/packages"]
        mock_getusersitepackages.return_value = "/fake/user/site/packages"
        mock_os_path_dirname = "/fake/os/path"

        with patch("os.path.dirname",
                   return_value=mock_os_path_dirname) as mock_dirname:
            with patch("os.__file__", return_value="/fake/os/__file__"):
                # Volání funkce bez jakýchkoli argumentů
                result = get_ignore_paths()

                # Ověřujeme, že všechny cesty byly přidány
                expected = [
                    mock_os_path_dirname,  # Standardní knihovna
                    "/fake/site/packages",  # Nainstalované balíčky
                    "/fake/user/site/packages",  # Uživatelské balíčky
                ]
                self.assertEqual(result, expected)

                # Volání abspath by mělo proběhnout pro standardní knihovnu
                mock_abspath.assert_any_call(mock_os_path_dirname)
                # A pro každou cestu z getsitepackages a getusersitepackages
                mock_abspath.assert_any_call("/fake/site/packages")
                mock_abspath.assert_any_call("/fake/user/site/packages")

    @patch("os.path.abspath")
    @patch("site.getsitepackages")
    @patch("site.getusersitepackages")
    def test_add_path(self, mock_getusersitepackages, mock_getsitepackages,
                      mock_abspath):
        # Nastavíme, aby abspath vracel svůj argument
        mock_abspath.side_effect = lambda path: path
        mock_getsitepackages.return_value = ["/fake/site/packages"]
        mock_getusersitepackages.return_value = "/fake/user/site/packages"
        mock_os_path_dirname = "/fake/os/path"

        with patch("os.path.dirname",
                   return_value=mock_os_path_dirname) as mock_dirname:
            with patch("os.__file__", return_value="/fake/os/__file__"):
                # Volání funkce s přidanou cestou
                result = get_ignore_paths(add_path=["/additional/path"])

                # Ověřujeme, že přidaná cesta je ve výsledku
                expected = [
                    mock_os_path_dirname,
                    "/fake/site/packages",
                    "/fake/user/site/packages",
                    "/additional/path"  # Přidaná cesta
                ]
                self.assertEqual(result, expected)

                # Kontrolujeme volání abspath
                mock_abspath.assert_any_call(mock_os_path_dirname)
                mock_abspath.assert_any_call("/fake/site/packages")
                mock_abspath.assert_any_call("/fake/user/site/packages")
                mock_abspath.assert_any_call(
                    "/additional/path")  # Kontrola pro přidanou cestu


    def test_unexpected_error(self):
        # Simulace neočekávané chyby při volání get_ignore_paths
        with patch("os.path.abspath",
                   side_effect=Exception("Unexpected error")):
            with self.assertRaises(VerifyUnexpectedError):
                get_ignore_paths()

    @patch("os.path.abspath")
    @patch("site.getsitepackages")
    @patch("site.getusersitepackages")
    def test_empty_add_path(self, mock_getusersitepackages,
                            mock_getsitepackages, mock_abspath):
        # Nastavíme, aby abspath vracel svůj argument
        mock_abspath.side_effect = lambda path: path
        mock_getsitepackages.return_value = ["/fake/site/packages"]
        mock_getusersitepackages.return_value = "/fake/user/site/packages"
        mock_os_path_dirname = "/fake/os/path"

        with patch("os.path.dirname",
                   return_value=mock_os_path_dirname) as mock_dirname:
            with patch("os.__file__", return_value="/fake/os/__file__"):
                # Volání funkce s prázdným seznamem pro add_path
                result = get_ignore_paths(add_path=[])

                # Očekáváme, že nic nebude přidáno
                expected = [
                    mock_os_path_dirname,
                    "/fake/site/packages",
                    "/fake/user/site/packages",
                ]
                self.assertEqual(result, expected)

                # Kontrolujeme volání abspath
                mock_abspath.assert_any_call(mock_os_path_dirname)
                mock_abspath.assert_any_call("/fake/site/packages")
                mock_abspath.assert_any_call("/fake/user/site/packages")
                # Pro prázdný add_path by se normalize_paths nemělo volat s žádnými cestami

    @patch("os.path.abspath")
    @patch("site.getsitepackages")
    @patch("site.getusersitepackages")
    def test_none_add_path(self, mock_getusersitepackages, mock_getsitepackages,
                           mock_abspath):
        # Nastavíme, aby abspath vracel svůj argument
        mock_abspath.side_effect = lambda path: path
        mock_getsitepackages.return_value = ["/fake/site/packages"]
        mock_getusersitepackages.return_value = "/fake/user/site/packages"
        mock_os_path_dirname = "/fake/os/path"

        with patch("os.path.dirname",
                   return_value=mock_os_path_dirname) as mock_dirname:
            with patch("os.__file__", return_value="/fake/os/__file__"):
                result = get_ignore_paths(add_path=None)

                # Očekáváme stejné chování jako bez přidané cesty
                expected = [
                    mock_os_path_dirname,
                    "/fake/site/packages",
                    "/fake/user/site/packages",
                ]
                self.assertEqual(result, expected)

                # Kontrolujeme volání abspath
                mock_abspath.assert_any_call(mock_os_path_dirname)
                mock_abspath.assert_any_call("/fake/site/packages")
                mock_abspath.assert_any_call("/fake/user/site/packages")
                # Pro None add_path by se normalize_paths nemělo volat

    def test_invalid_add_path(self):
        # Volání funkce s neplatným typem pro add_path
        with self.assertRaises(InvalidPathInputError):
            get_ignore_paths(add_path=123)  # Číslo místo seznamu nebo cesty


# Lokální zpuštění testů
if __name__ == "__main__":
    unittest.main()

