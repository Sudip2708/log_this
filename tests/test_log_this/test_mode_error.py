import pytest
from log_this_old.log_this import log_this


@pytest.mark.parametrize("error_mode", [-1, 5, 'error'])
def test_error_mode(capture_logs, mock_function, error_mode):
    """
    Test, zda dekorátor správně zachytí nesprávně uvedenou hodnotu pro mode.

    Args:
        capture_logs: Fixture pro zachytávání logů
        mock_function: Fixture s mock funkcí
        error_mode: Nesprávné parametry pro vyvolání výjimky
    """

    # Použití dekorátoru
    @log_this(mode=error_mode)
    def decorated_mock_function(x, y):
        return mock_function(x, y)

    # Získání výsledku a logu
    result = decorated_mock_function(2, 3)
    log_output = capture_logs.getvalue()

    # Kontrola správného výsledku
    assert result == 5, f"Neočekávaný výsledek: {result}"

    # Kontrola, zda došlo k jednořádkovému výpis
    assert "LogThis ERROR" in log_output, "Není uvedeno úvodní info: LogThis ERROR."
    assert "not defined" in log_output, "Není uveden řádek s info o chybě."
    assert "Function" in log_output, "Není uveden řádek s názvem funkce."
    assert "File" in log_output, "Není uveden řádek s odkazem na soubor."
    assert len(log_output.splitlines()) == 5, f"Očekávány 5 řádků (4+mezera). Nalezeno: {len(log_output.splitlines())}."


@pytest.mark.parametrize("error_mode", [-1, 5, 'error'])
def test_error_mode_complex_object(capture_logs, complex_object, error_mode):
    """
    Test, zda dekorátor správně zachytí nesprávně uvedenou hodnotu pro mode.

    Args:
        capture_logs: Fixture pro zachytávání logů
        complex_object: Fixture s mock komplexním objektem
        error_mode: Nesprávné parametry pro vyvolání výjimky
    """

    # Použití dekorátoru
    @log_this(mode=error_mode)
    def test_function(obj):
        return obj.public_attr

    # Získání výsledku a logu
    result = test_function(complex_object)
    log_output = capture_logs.getvalue()

    # Kontrola správného výsledku
    assert result == 42

    # Kontrola, zda došlo k výpisu
    assert "LogThis ERROR" in log_output, f"Test pro ověření dekorátoru s mode {error_mode} pro komplexní objekt selhal."
