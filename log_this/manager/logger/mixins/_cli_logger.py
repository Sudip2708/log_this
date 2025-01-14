import logging
from log_this.manager.ansi_styler import cli_format

class CliLoggerMixin:

    # Předkonfigurované loggery
    CLI_LOGGER_CONFIG = {
        'name': 'LogThis.CLI',
        'level': logging.INFO,
        'propagate': True,
        'log_to_file': False,
        'formatter': logging.Formatter(
            cli_format('%(levelname)s', '%(message)s', '%(extra)s')
        )
    }

    @classmethod
    def cli_logger(cls) -> logging.Logger:
        """Logger pro CLI komunikaci."""
        return cls.get_logger(**cls.CLI_LOGGER_CONFIG)

