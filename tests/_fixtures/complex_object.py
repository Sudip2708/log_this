"""
**Funkce `complex_object`:**
   - **Co dělá:** Vytváří instanci třídy `NestedObject` s několika atributy, která slouží jako testovací data.
   - **Jak funguje:** Vrací objekt obsahující veřejné atributy, soukromé atributy a vnořená data (seznamy, slovníky).
   - **Příklad použití:**
     ```python
     def test_complex_object_structure(complex_object):
         assert complex_object.public_attr == 42
         assert complex_object.nested['list'] == [1, 2, 3]
     ```
"""
import pytest

@pytest.fixture
def complex_object():
    """Fixture pro vytvoření komplexního objektu pro testování serializace.

    Returns:
        object: Komplexní objekt s vnořenými atributy
    """
    class NestedObject:
        def __init__(self):
            self.public_attr = 42
            self._private_attr = "secret"
            self.nested = {
                'list': [1, 2, 3],
                'dict': {'key': 'value'}
            }

    return NestedObject()