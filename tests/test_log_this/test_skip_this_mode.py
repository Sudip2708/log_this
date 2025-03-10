import pytest
from log_this_old.log_this import log_this


@pytest.mark.parametrize("skip_mode", [0, 'skip_this', False, None, ''])
def test_skip_this_mode(capture_logs, mock_function, skip_mode):
    """
    Test, zda dekorátor správně vyhodnotí přednastavené mody pro přeskočení logování.

    Args:
        capture_logs: Fixture pro zachytávání logů
        mock_function: Fixture s mock funkcí
        skip_mode: Parametr pro přeskočení logování
    """

    # Použití dekorátoru
    @log_this(mode=skip_mode)
    def decorated_mock_function(x, y):
        return mock_function(x, y)

    # Získání výsledku a logu
    result = decorated_mock_function(2, 3)
    log_output = capture_logs.getvalue()

    # Kontrola správného výsledku
    assert result == 5, f"Neočekávaný výsledek: {result}"

    # Kontrola, zda nedošlo k žádnému logování
    assert log_output == "", f"Pro mode {skip_mode} by nemělo dojít k logování"


@pytest.mark.parametrize("skip_mode", [0, 'skip_this', False, None, ''])
def test_skip_this_mode_complex_object(capture_logs, complex_object, skip_mode):
    """
    Test, zda dekorátor správně funguje i pro komplexní objekty.

    Args:
        capture_logs: Fixture pro zachytávání logů
        complex_object: Fixture s mock komplexním objektem
        skip_mode: Parametr pro přeskočení logování
    """

    # Použití dekorátoru
    @log_this(mode=skip_mode)
    def test_function(obj):
        return obj.public_attr

    # Získání výsledku a logu
    result = test_function(complex_object)
    log_output = capture_logs.getvalue()

    # Kontrola správného výsledku
    assert result == 42

    # Kontrola, zda došlo k výpisu
    assert log_output == "", f"Test pro ověření dekorátoru s mode {skip_mode} pro komplexní objekt selhal."
