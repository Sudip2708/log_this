# log_this/manager/config/cli/utils/_logging.py
import logging

def setup_logging() -> None:
    """Nastaví základní konfiguraci pro logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s'
    )


# log_this/manager/config/cli/_setup_logging.py
import logging

def setup_logging():
    """Nastaví logování pro celý systém."""
    logger = logging.getLogger('LogThis')  # Globální loger pro celou aplikaci
    logger.setLevel(logging.DEBUG)

    # Vytvoření handleru pro výstup do konzole
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    return logger
