"""
Testy pokrývají:
- Základní scénáře ověřování
- Chování při různých typech vstupů
- Generování chybových zpráv
- Vnořená volání
- Kontrolu dokumentace a typových anotací
- Základní měření výkonnosti

Poznámky k testům:
- Používá `pytest` pro psaní testů
- Každý test má jasný popis a účel
- Pokrývá jak pozitivní, tak negativní scénáře
- Kontroluje dokumentaci a typové anotace
- Obsahuje i orientační test výkonnosti

Doporučení pro spuštění:
1. Nainstalujte `pytest`: `pip install pytest`
2. Uložte testy do souboru `test_verify.py`
3. Spusťte příkazem `pytest test_verify.py`
"""

import pytest
import inspect

# Import testovaného modulu (předpokládám název souboru verify.py)
from ..verify import (
    verify,
    verify_bool,
    verify_call,
    VerifyError,
    SafeVerifyError
)


class TestVerificationLibrary:
    """
    Komplexní testovací sada pro knihovnu ověřování.

    Pokrývá scénáře:
    - Správné chování pri splnění podmínek
    - Selhání ověření s různými typy vstupů
    - Chování při neočekávaných vstupech
    - Kontrola generování chybových zpráv
    """

    def test_verify_with_boolean_true(self):
        """Test ověření s boolean hodnotou True."""
        assert verify(True) is True

    def test_verify_with_boolean_false(self):
        """Test selhání ověření s boolean hodnotou False."""
        with pytest.raises(VerifyError):
            verify(False)

    def test_verify_with_callable_true(self):
        """Test ověření s callable vracejícím True."""

        def test_func():
            return True

        assert verify(test_func) is True

    def test_verify_with_callable_false(self):
        """Test selhání ověření s callable vracejícím False."""

        def test_func():
            return False

        with pytest.raises(VerifyError):
            verify(test_func)

    def test_verify_with_custom_exception(self):
        """Test použití vlastní výjimky."""

        class CustomError(Exception):
            pass

        with pytest.raises(CustomError):
            verify(False, exception_type=CustomError)

    def test_verify_with_custom_message(self):
        """Test ověření s vlastní chybovou zprávou."""
        with pytest.raises(VerifyError, match="Vlastní zpráva"):
            verify(False, message="Vlastní zpráva")

    def test_verify_call_with_exception_in_callable(self):
        """Test chování při výjimce uvnitř callable."""

        def error_func():
            raise ValueError("Testovací výjimka")

        with pytest.raises(SafeVerifyError, match="Chyba při volání"):
            verify(error_func)

    def test_verify_bool_type_error(self):
        """Test chování při neplatném typu pro boolean."""
        with pytest.raises(SafeVerifyError, match="Neplatný typ"):
            verify_bool(None)  # type: ignore

    def test_verify_call_type_error(self):
        """Test chování při neplatném callable."""
        with pytest.raises(SafeVerifyError):
            verify_call("not a callable")  # type: ignore

    def test_error_message_generation(self):
        """Test generování chybové zprávy."""

        def test_method():
            try:
                verify(False)
            except VerifyError as e:
                # Kontrola, zda zpráva obsahuje informace o volání
                assert "test_error_message_generation" in str(e)
                assert __file__ in str(e)
                raise

        with pytest.raises(VerifyError):
            test_method()

    def test_nested_verify_calls(self):
        """Test vnořených ověřovacích volání."""

        def outer_func():
            def inner_func():
                return False

            verify(inner_func)

        with pytest.raises(VerifyError):
            outer_func()

    def test_performance_overhead(self):
        """Orientační test výkonnosti."""
        import timeit

        # Měření času pro jednoduché ověření
        def test_performance():
            verify(True)

        execution_time = timeit.timeit(test_performance, number=10000)

        # Orientační limit (velmi subjektivní)
        assert execution_time < 0.5, "Příliš dlouhá doba provádění ověření"


def test_docstrings_and_type_hints():
    """
    Kontrola dokumentace a typových anotací.
    Zajišťuje, že všechny veřejné funkce mají docstrings a správné anotace.
    """
    public_functions = [verify, verify_bool, verify_call]

    for func in public_functions:
        # Kontrola existence docstrings
        assert func.__doc__ is not None, f"{func.__name__} postrádá docstring"

        # Kontrola typových anotací
        signature = inspect.signature(func)
        for param_name, param in signature.parameters.items():
            assert param.annotation != inspect.Parameter.empty, \
                f"Parametr {param_name} funkce {func.__name__} postrádá typovou anotaci"

        # Kontrola návratové anotace
        return_annotation = signature.return_annotation
        assert return_annotation != inspect.Signature.empty, \
            f"Funkce {func.__name__} postrádá anotaci návratu"


if __name__ == "__main__":
    pytest.main([__file__])
