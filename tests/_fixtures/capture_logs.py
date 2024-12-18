"""
**Funkce `capture_logs`:**
   - **Co dělá:** Tato funkce zachytává logovací výstup během testování. Pomocí `yield log_capture` vrací objekt `StringIO`, který ukládá logy.
   - **Jak funguje:**
     - Vytvoří objekt `StringIO`, kam se zapisují logy.
     - Přidá do hlavního loggeru nový handler pro tento objekt.
     - `yield log_capture` vrací objekt pro zachytávání logů do testu.
     - Po dokončení testu se handler odstraní a uzavře.
   - **Příklad použití:**
     ```python
     def test_logging_output(capture_logs):
         logging.debug("Testovací log")
         assert "Testovací log" in capture_logs.getvalue()
     ```
"""
import pytest
import logging
import io

@pytest.fixture
def capture_logs():
    """Fixture pro zachycení log výstupů.

    Umožňuje zachytávat logger výstupy pro následnou analýzu v testech.

    Returns:
        io.StringIO: Objekt StringIO s zachycenými log zprávami
    """
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)

    yield log_capture

    root_logger.removeHandler(handler)
    handler.close()