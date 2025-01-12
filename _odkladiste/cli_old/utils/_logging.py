# log_this/manager/config/cli/utils/_logging.py
import logging

def setup_logging() -> None:
    """Nastaví základní konfiguraci pro logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s'
    )