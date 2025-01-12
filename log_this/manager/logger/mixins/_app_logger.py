import logging

class AppLoggerMixin:

    # Předkonfigurované loggery
    APP_LOGGER_CONFIG = {
        'name': 'LogThis.App',
        'level': logging.DEBUG,
        'propagate': True,
        'log_to_file': False,
        'formatter': logging.Formatter('%(message)s')
    }

    @classmethod
    def app_logger(cls) -> logging.Logger:
        """Logger pro hlavní aplikační logy."""
        return cls.get_logger(**cls.APP_LOGGER_CONFIG)

