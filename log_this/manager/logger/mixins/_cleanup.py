import logging

class CleanupMixin:

    @classmethod
    def cleanup(cls) -> None:
        """
        Vyčistí všechny handlery a zavře soubory.
        Vhodné volat při ukončení aplikace.
        """
        for logger in cls._loggers.values():
            for handler in logger.handlers[:]:
                if isinstance(handler, logging.FileHandler):
                    handler.close()
                logger.removeHandler(handler)
        cls._loggers.clear()