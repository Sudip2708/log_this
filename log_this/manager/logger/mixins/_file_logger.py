import logging

class FileLoggerMixin:

    # Předkonfigurované loggery
    FILE_LOGGER_CONFIG = {
        'name': 'LogThis',
        'level': logging.CRITICAL,
        'propagate': False,
        'log_to_file': True,
    }

    @classmethod
    def file_logger(cls) -> logging.Logger:
        """Logger pro hlavní aplikační logy."""
        return cls.get_logger(**cls.FILE_LOGGER_CONFIG)

