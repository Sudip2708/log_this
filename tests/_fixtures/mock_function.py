"""
**Funkce `mock_function`:**
   - **Co dělá:** Poskytuje jednoduchou funkci pro sčítání dvou čísel, kterou lze používat v testech.
   - **Jak funguje:** Vrací vnořenou funkci `_mock_function`, která přidává dvě čísla.
   - **Příklad použití:**
     ```python
     def test_mock_function(mock_function):
         result = mock_function(2, 3)
         assert result == 5
     ```
"""
import pytest

@pytest.fixture
def mock_function():
    """Fixture pro vytvoření jednoduché mock funkce pro testování logování.

    Returns:
        Callable: Mockovaná funkce pro testovací účely
    """
    def _mock_function(x: int, y: int) -> int:
        return x + y

    return _mock_function