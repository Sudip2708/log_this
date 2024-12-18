import pytest
from log_this.log_this import log_this


@pytest.mark.parametrize("one_line_mode", [1, 'one_line', True])
def test_one_line_mode(capture_logs, mock_function, one_line_mode):
    """
    Test, zda dekorátor správně vyhodnotí přednastavené mody pro jednořádkové logování.

    Args:
        capture_logs: Fixture pro zachytávání logů
        mock_function: Fixture s mock funkcí
        one_line_mode: Parametr pro jednořádkové logování
    """

    # Použití dekorátoru
    @log_this(mode=one_line_mode)
    def decorated_mock_function(x, y):
        return mock_function(x, y)

    # Získání výsledku a logu
    result = decorated_mock_function(2, 3)
    log_output = capture_logs.getvalue()

    # Kontrola správného výsledku
    assert result == 5, f"Neočekávaný výsledek: {result}"

    # Kontrola, zda došlo k jednořádkovému výpisu
    assert "INFO LogThis('one_line')" in log_output, "Není uvedeno úvodní info: INFO LogThis('one_line')."
    assert "mock_function(2, 3)" in log_output, "Není uvedena funkce, která se loguje. Např: mock_function(2, 3)."
    assert len(log_output.splitlines()) == 2, f"Očekávány 2 řádky (1+mezera). Nalezeno: {len(log_output.splitlines())}."


@pytest.mark.parametrize("one_line_mode", [1, 'one_line', True])
def test_one_line_mode_complex_object(capture_logs, complex_object, one_line_mode):
    """
    Test, zda dekorátor správně funguje i pro komplexní objekty.

    Args:
        capture_logs: Fixture pro zachytávání logů
        complex_object: Fixture s mock komplexním objektem
        one_line_mode: Parametr pro jednořádkové logování
    """

    # Použití dekorátoru
    @log_this(mode=one_line_mode)
    def test_function(obj):
        return obj.public_attr

    # Získání výsledku a logu
    result = test_function(complex_object)
    log_output = capture_logs.getvalue()

    # Kontrola správného výsledku
    assert result == 42

    # Kontrola, zda došlo k výpisu
    assert "INFO LogThis('one_line')" in log_output, f"Test pro ověření dekorátoru s mode {one_line_mode} pro komplexní objekt selhal."
