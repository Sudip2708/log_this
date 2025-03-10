import pytest
from log_this_old.modes.utils._get_limited_docstring import get_limited_docstring


@pytest.fixture
def sample_docstring():
    """
    Fixture poskytující ukázkový docstring pro testy.

    Returns:
        str: Docstring s více řádky.
    """
    return "Line 1\nLine 2\nLine 3"


def test_get_limited_docstring_short(sample_docstring):
    """
    Test, zda funkce get_limited_docstring správně ořízne docstring na maximální počet řádků.

    Args:
        sample_docstring (str): Docstring obsahující několik řádků.
    """
    # Očekávaný výsledek: první dva řádky, zbytek označený ' (...)'
    assert get_limited_docstring(sample_docstring, max_lines=2) == "Line 1\nLine 2 (...)"


def test_get_limited_docstring_exact(sample_docstring):
    """
    Test, zda funkce get_limited_docstring vrátí přesně požadovaný počet řádků.

    Args:
        sample_docstring (str): Docstring obsahující několik řádků.
    """
    # Očekávaný výsledek: všechny tři řádky
    assert get_limited_docstring(sample_docstring, max_lines=3) == "Line 1\nLine 2\nLine 3"


def test_get_limited_docstring_empty():
    """
    Test, zda funkce get_limited_docstring vrátí "N/A" pro prázdný docstring.

    Args:
        None
    """
    # Očekávaný výsledek: "N/A" pro prázdný docstring
    assert get_limited_docstring("") == "N/A"


def test_get_limited_docstring_no_docstring():
    """
    Test, zda funkce get_limited_docstring vrátí "N/A", pokud není docstring poskytnut.

    Args:
        None
    """
    # Očekávaný výsledek: "N/A" pro None jako vstup
    assert get_limited_docstring(None) == "N/A"

def test_get_limited_docstring_all(sample_docstring):
    """
    Test, zda funkce get_limited_docstring vrátí celý docstring,
    pokud je max_lines nastaveno na 'all'.

    Args:
        sample_docstring (str): Docstring obsahující několik řádků.
    """
    # Očekávaný výsledek: celý docstring
    assert get_limited_docstring(sample_docstring, max_lines='all') == "Line 1\nLine 2\nLine 3"
