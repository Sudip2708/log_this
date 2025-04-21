import logging
from typing import Optional

def create_context_logger(
        log_file: Optional[str] = None,
        log_level: int = logging.INFO
) -> logging.Logger:
    """
    Vytvoří konfigurovatelný logger s možností výstupu do souboru.

    :param log_file: Cesta k log souboru
    :param log_level: Úroveň logování
    :return: Nakonfigurovaný logger
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Formátování logu
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Konzolový handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Volitelný souborový handler
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger