import logging

def setup_cli_logger():
    """Nastaví logger pro CLI."""
    logger = logging.getLogger('CLI')

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(levelname)s: %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        logger.setLevel(logging.INFO)  # Nebo jiná úroveň podle potřeby

    return logger
