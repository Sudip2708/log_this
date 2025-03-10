from logging.handlers import RotatingFileHandler
from typing import Optional
import logging
from pathlib import Path

class CreateFileHandlerMixin:

    # Konstanty pro formátování
    DEFAULT_FILE_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


    # Konstanty pro rotující logy
    DEFAULT_MAX_BYTES = 1_000_000  # 1MB
    DEFAULT_BACKUP_COUNT = 3
    DEFAULT_LOG_DIR = Path("logs")

    @classmethod
    def _create_file_handler(
            cls,
            filename: Optional[str] = None,
            max_bytes: int = DEFAULT_MAX_BYTES,
            backup_count: int = DEFAULT_BACKUP_COUNT
    ) -> logging.FileHandler:
        """
        Vytvoří handler pro logování do souboru s automatickou rotací.
        """

        if filename is None:
            raise ValueError(
                "Parameter 'filename' is required and cannot be None.")


        log_path = cls.DEFAULT_LOG_DIR / (filename or "app.log")
        log_path.parent.mkdir(exist_ok=True)

        handler = RotatingFileHandler(
            log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding='utf-8'
        )

        formatter = logging.Formatter(
            cls.DEFAULT_FILE_FORMAT,
            datefmt=cls.DEFAULT_DATE_FORMAT
        )
        handler.setFormatter(formatter)

        return handler