import logging


def loger_settings():
    """
    Nastaví logger pro aplikaci.

    Tato funkce konfiguruje základní nastavení loggeru, včetně úrovně zachycení
    logů (DEBUG), formátu logů a handleru pro výstup na standardní výstup.

    Returns:
        logging.Logger: Konfigurovaný logger, který je připraven k použití.
    """

    # Vytvoření, načtení loggeru
    logger = logging.getLogger('LogThis')


    # Kontrola zda má definované parametry
    if not logger.handlers:

        # Vyčištěění případných handlerů
        logger.handlers.clear()

        # Vytvoření handleru pro výstup na konzoli
        console_handler = logging.StreamHandler()

        # Nastavení formátu logování
        formatter = logging.Formatter('%(message)s')
        console_handler.setFormatter(formatter)

        # Přidání handleru do loggeru
        logger.addHandler(console_handler)

    # Nastavení úrovně logování
    logger.setLevel(logging.DEBUG)

    return logger

