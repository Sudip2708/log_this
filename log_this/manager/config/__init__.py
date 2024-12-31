from ._config_base import LogThisConfig
from .get_config import get_config

__all__ = [
    "LogThisConfig",  # Singleton třída pro správu konfigurace.
    "get_config",  # Hlavní funkce vracející singleton instanci třífy LogThisConfig.
]