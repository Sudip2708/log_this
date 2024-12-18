from .config import LogThisConfig
# from ._loader_mixin import ConfigLoaderMixin

__all__ = [
    "LogThisConfig",  # Singleton třída pro konfuguraci (použito ve funkci get_config)
    # "ConfigLoaderMixin",  # Mixin přidávající hlavní třídě automatické načítání a validaci konfigurace (použito ve LogThisConfig)
]