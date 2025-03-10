import pytest
from log_this_old.log_this import log_this


@pytest.mark.parametrize("detailed_mode", [3, 'detailed'])
def test_detailed_mode(capture_logs, mock_function, detailed_mode):
    """
    Test, zda dekorátor správně vyhodnotí přednastavené mody pro detailní logování (6 řádek).

    Args:
        capture_logs: Fixture pro zachytávání logů
        mock_function: Fixture s mock funkcí
        detailed_mode: Parametr pro detailní logování
    """

    # Použití dekorátoru
    @log_this(mode=detailed_mode)
    def decorated_mock_function(x, y):
        return mock_function(x, y)

    # Získání výsledku a logu
    result = decorated_mock_function(2, 3)
    log_output = capture_logs.getvalue()

    # Kontrola správného výsledku
    assert result == 5, f"Neočekávaný výsledek: {result}"

    # Kontrola, zda došlo k výpis
    assert "START LogThis('detailed')" in log_output, "Není uvedeno úvodní info: START LogThis('detailed')."
    assert "mock_function" in log_output, "V úvodu není uveden název funkce funkce."
    assert "File" in log_output, "Není uvedena cesta k souboru."
    assert "Input parameters" in log_output, "Není uveden řádek s parametry."
    assert "Input kwords" in log_output, "Řádek s 'Input parameters' neobsahuje 'Input kwords'."
    assert "Outcome" in log_output, "Není uveden řádek s výstupem."
    assert "Type" in log_output, "Řádek s 'Outcome' neobsahuje 'Type'."
    assert "Running time" in log_output, "Není uveden řádek s dobou běhu."
    assert "Memory usage" in log_output, "Řádek s 'Running time'  neobsahuje 'Memory usage'."
    assert "END LogThis('detailed')" in log_output, "Není uvedeno závěrečné info: END LogThis('detailed')."
    assert "Log duration" in log_output, "Poslední řádek neobsahuje 'Log duration'."
    assert len(log_output.splitlines()) == 7, f"Očekávány 7 řádků (6+mezera). Nalezeno: {len(log_output.splitlines())}."


@pytest.mark.parametrize("detailed_mode", [3, 'detailed'])
def test_detailed_mode_complex_object(capture_logs, complex_object, detailed_mode):
    """
    Test, zda dekorátor správně funguje i pro komplexní objekty.

    Args:
        capture_logs: Fixture pro zachytávání logů
        complex_object: Fixture s mock komplexním objektem
        detailed_mode: Parametr pro detailní logování
    """

    # Použití dekorátoru
    @log_this(mode=detailed_mode)
    def test_function(obj):
        return obj.public_attr

    # Získání výsledku a logu
    result = test_function(complex_object)
    log_output = capture_logs.getvalue()

    # Kontrola správného výsledku
    assert result == 42

    # Kontrola, zda došlo k výpisu
    assert "START LogThis('detailed')" in log_output, f"Test pro ověření dekorátoru s mode {detailed_mode} pro komplexní objekt selhal."


@pytest.mark.parametrize("detailed_mode", [3, 'detailed'])
def test_detailed_mode_exception(capture_logs, detailed_mode):
    """
    Test, zda dekorátor správně loguje výjimky, když volaná funkce selže.

    Args:
        capture_logs: Fixture pro zachytávání logů
        detailed_mode: Parametr pro detailní logování
    """

    # Funkce, která vyvolá výjimku
    @log_this(mode=detailed_mode)
    def failing_function(x):
        if x < 0:
            raise ValueError("Negative value not allowed!")
        return x

    # Zachycení výjimky
    with pytest.raises(ValueError, match="Negative value not allowed!"):
        failing_function(-1)

    # Získání logu
    log_output = capture_logs.getvalue()

    # Kontrola, zda log obsahuje správné informace o výjimce
    assert "START LogThis('detailed')" in log_output, "Není uvedeno úvodní info: START LogThis('detailed')."
    assert "failing_function" in log_output, "V logu není uveden název funkce."
    assert "Outcome: Raised exception ValueError" in log_output, "Log neobsahuje informaci o vyvolané výjimce."
    assert "Negative value not allowed!" in log_output, "Log neobsahuje text výjimky."
    assert "END LogThis('detailed')" in log_output, "Není uvedeno závěrečné info: END LogThis('detailed')."
