import pytest
import logging
from log_this_old.manager.logger import get_logger
import io


@pytest.fixture
def logger():
    """
    Fixture, která poskytuje logger pro testy.

    Returns:
        logging.Logger: Logger, který byl vytvořen pomocí loger_settings().
    """
    return get_logger()


@pytest.fixture
def capture_logs(logger):
    """Fixture pro zachycení log výstupů.

    Umožňuje zachytávat logger výstupy pro následnou analýzu v testech.

    Returns:
        io.StringIO: Objekt StringIO s zachycenými log zprávami
    """
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)

    yield log_capture

    logger.removeHandler(handler)
    handler.close()


def test_logger_instance(logger):
    """Ověří, instance loggeru."""
    assert isinstance(logger, logging.Logger), \
        (f"Logger by měl být typu logging.Logger. "
         f"Zjištěná instance: {type(logger)}")


def test_logger_name(logger):
    """Ověří, zda jména logeru."""
    assert logger.name == 'LogThis', \
        (f"Jméno loggeru by mělo být 'LogThis'. "
         f"Zjištěné jméno: {repr(logger.name)}")


def test_logger_propagate(logger):
    """Ověří, zda nastavení pro loger se nepřepisuje do root logeru."""
    assert logger.propagate == False, \
        (f"Hodnota pro propagate by měla být False. "
         f"Zjištěná hodnota: {logger.propagate}")


def test_logger_handlers(logger):
    """Ověří, že logger má jen jeden handler."""
    assert len(logger.handlers) == 1, \
        (f"Logger by měl mít pouze jeden handler pro výpis do konzole. "
         f"Počet zjištěných handlerů: {len(logger.handlers)}")


def test_logger_console_handler(logger):
    """Ověří, že handler je console_handler a jeho typ."""
    console_handler = logger.handlers[0]
    assert isinstance(console_handler, logging.StreamHandler), \
        (f"Handler by měl být typu logging.StreamHandler. "
         f"Zjištěný typ handleru: {type(console_handler)}")


def test_logger_formatter(logger):
    """Ověří, že handler má nastavený formatter."""
    console_handler = logger.handlers[0]
    formatter = console_handler.formatter
    assert isinstance(formatter, logging.Formatter), \
        (f"Formatter by měl být typu logging.Formatter."
         f"Zjištěný typ formatteru: {type(formatter)}")


def test_logger_formatter_setting(logger):
    """Ověří, že handler má nastavený formatter."""
    console_handler = logger.handlers[0]
    formatter = console_handler.formatter
    assert formatter._fmt == '%(message)s', \
        (f"Formát formatteru by měl být '%(message)s'. "
         f"Zjištěné nastavení: {repr(formatter._fmt)}")


def test_logger_level(logger):
    """Ověří, že logger má nastavenou úroveň na DEBUG."""
    assert logger.level == logging.DEBUG, \
        (f"Úroveň loggeru by měla být nastavena na DEBUG. "
         f"Zjištěná hodnota: {logging.getLevelName(logger.level)}")


def test_logger_output_format(logger, capture_logs):
    """Ověří, zda logger správně zachytí a přepíše zprávi."""
    logger.debug('Test message')  # Vytvoření testovací zprávy
    captured = capture_logs.getvalue()  # Získání zachyceného výstupu
    assert 'Test message' in captured, \
        (f"Zachycený log by měl obsahovat 'Test message'. "
         f"Zachycený obsah: {repr(captured)}")


def test_logger_does_not_duplicate_handlers(logger):
    """Ověří, zda funkce loger_settings nepřidá další handler, pokud již existuje."""

    # Počet handlerů po prvním volání
    initial_handlers_count = len(logger.handlers)

    # Opětovné volání funkce
    get_logger()

    # Počet handlerů po druhém volání
    final_handlers_count = len(logger.handlers)

    # Ověření, že počet handlerů zůstal stejný
    assert initial_handlers_count == final_handlers_count, \
        (f"Počet handlerů by se neměl změnit při opětovném volání loger_settings. "
         f"První volání: {initial_handlers_count}, "
         f"Opětovné volání: {len(logger.handlers)}")
