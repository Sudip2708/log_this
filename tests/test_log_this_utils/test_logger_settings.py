import pytest
import logging
from log_this.modes.utils import loger_settings


@pytest.fixture
def logger():
    """
    Fixture, která poskytuje logger pro testy.

    Returns:
        logging.Logger: Logger, který byl vytvořen pomocí loger_settings().
    """
    return loger_settings()


def test_logger_creation(logger):
    """
    Test, zda funkce loger_settings správně vytváří logger.

    Args:
        logger (logging.Logger): Logger vytvořený pomocí loger_settings.
    """
    # Ověření, že vrácený logger má správné jméno
    assert isinstance(logger, logging.Logger), "Logger by měl být typu logging.Logger"
    assert logger.name == 'LogThis', "Jméno loggeru by mělo být 'LogThis'"


def test_logger_level(logger):
    """
    Test, zda funkce loger_settings nastaví správnou úroveň logování.

    Args:
        logger (logging.Logger): Logger vytvořený pomocí loger_settings.
    """
    # Ověření, že úroveň loggeru je nastavena na DEBUG
    assert logger.level == logging.DEBUG, "Úroveň loggeru by měla být DEBUG"


def test_logger_format(logger, capture_logs):
    """
    Test, zda logger správně zachytí zprávy.

    Args:
        logger (logging.Logger): Logger vytvořený pomocí loger_settings.
        capture_logs: Fixture pro zachytávání výstupu loggeru.
    """
    # Vytvoření testovací zprávy
    logger.debug('Testovací zpráva')

    # Získání zachyceného výstupu
    captured = capture_logs.getvalue()

    # Ověření, že výstup obsahuje správnou zprávu
    assert 'Testovací zpráva' in captured, "Log by měl obsahovat 'Testovací zpráva'"


def test_logger_adds_handler():
    """
    Test, zda funkce loger_settings přidá handler, pokud logger nemá žádný handler.
    """
    # Vytvoření loggeru pomocí funkce
    logger = loger_settings()

    # Ověření, že logger má alespoň jeden handler
    assert logger.hasHandlers(), "Logger by měl mít alespoň jeden handler"

    # Ověření typu prvního handleru
    assert any(isinstance(handler, logging.StreamHandler) for handler in
               logger.handlers), \
        "Logger by měl obsahovat StreamHandler"


def test_logger_does_not_duplicate_handlers():
    """
    Test, zda funkce loger_settings nepřidá další handler, pokud již existuje.
    """
    # Vytvoření loggeru pomocí funkce
    logger = loger_settings()

    # Počet handlerů po prvním volání
    initial_handlers_count = len(logger.handlers)

    # Opětovné volání funkce
    loger_settings()

    # Počet handlerů po druhém volání
    final_handlers_count = len(logger.handlers)

    # Ověření, že počet handlerů zůstal stejný
    assert initial_handlers_count == final_handlers_count, \
        "Počet handlerů by se neměl změnit při opětovném volání loger_settings"
