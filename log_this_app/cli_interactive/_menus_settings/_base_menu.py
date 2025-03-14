class BaseMenu:
    """Základní třída pro menu s automatickou inicializací menus_manager."""

    def __init__(self, menus_manager):
        self.mm = menus_manager