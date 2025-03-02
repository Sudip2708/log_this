from abc import ABC

from ._init_data import (
    InputManager,
    ResponseManager,
    MenuRenderer,
    MenusManager
)


class InitMethodMixin(ABC):
    """Mixin pro navigaci v interaktivním menu"""


    def _initialize(self, menu_name):
        """Metoda pro inicializaci třídy InteractiveCli"""

        # Napojení manažera pro vstup od uživatele
        self.input_manager = InputManager(self)

        # Napojení manažera pro správu odpovědí
        self.response_manager = ResponseManager(self)

        # Napojení renderu pro zobrazení menu
        self.menu_renderer = MenuRenderer(self)

        # Napojení managera spravující jednotlivá menu
        self.menus_manager = MenusManager(self)

        # Zápis atributtu pro název zobrazovaného menu
        self.menu_name = menu_name

        # Zápis atributu pro data zobrazovaného menu
        self.menu = self.menus_manager.get_menu(self.menu_name)
