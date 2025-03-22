from functools import partial
from typing import Dict, Optional, Tuple

# Import pro typovou analýzu
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..menus_manager import MenusManager


class BaseMenu:
    """
    Základní třída pro interaktivní menu.

    Poskytuje základní funkcionalitu pro správu nabídek menu, jejich nápovědy a přechod mezi menu.
    """

    # Definice povinných atributů menu
    _menu_key: Optional[str] = None
    _previous_menu_key: Optional[str] = None
    _menu_items: Optional[Dict[str, Dict[str, str]]] = None

    # Výchozí nadpis menu
    title: str = "VYBERTE ÚKON:"

    def __init__(self, menus_manager: "MenusManager") -> None:
        """
        Inicializuje instanci menu a propojí ji s manažerem menu.

        :param menus_manager: Instance MenusManager pro správu menu.
        """
        self.mm = menus_manager  # Hlavní správce menu, používaný jako `mm`
        self._config_manager = self.mm.config_manager
        self._items_manager = self._config_manager.items_manager

    @property
    def menu_help(self) -> Tuple[str, ...]:
        """
        Vrací textovou nápovědu k jednotlivým položkám menu.

        :return: Tuple obsahující texty nápovědy pro jednotlivé položky menu.
        """
        return tuple(
            f"{item['label']}: {item['help']}"
            for item in self._menu_items.values()
        ) if self._menu_items else ()

    """
    Následuje definice jedotlivých nabídek.
    Každá nabídka vrací tuple s řetězcem pro popis 
    a logikou která se má zpustit po vybrání položky.
    """

    def get_help_offer(self) -> Tuple[str, callable]:
        """
        Vrací nabídku pro zobrazení/skrytí nápovědy.

        :return: Dvojice obsahující text a metodu pro přepnutí nápovědy.
        """
        return (
            'Nápověda' if not self.mm.show_instruction else 'Skrýt nápovědu',
            self.mm.toggle_show_instruction
        )

    def get_previous_menu(self) -> Tuple[str, callable]:
        """
        Vrací nabídku pro návrat do předchozího menu.

        :return: Dvojice obsahující text a metodu pro návrat do předchozího menu.
        """
        return (
            "Zpět do předchozího menu",
            partial(self.mm.show_menu, self._previous_menu_key)
        )

    def get_close_offer(self) -> Tuple[str, callable]:
        """
        Vrací nabídku pro ukončení interaktivního režimu.

        :return: Dvojice obsahující text a metodu pro ukončení interaktivního režimu.
        """
        return (
            "Ukončit",
            self.mm.close_interactive_mode
        )

    def get_menu_offer(self, item_key: str) -> Tuple[str, callable]:
        """
        Vrací nabídku pro přechod na jinou nabídku v menu.

        :param item_key: Klíč položky menu.
        :return: Dvojice obsahující text a metodu pro přepnutí na zvolené menu.
        """
        return (
            f"• {self._menu_items[item_key]['label']}",
            partial(self.mm.show_menu, item_key)
        )

    def get_response_offer(self, item_key: str) -> Tuple[str, callable]:
        """
        Vrací nabídku pro vykonání akce spojené s danou položkou menu.

        :param item_key: Klíč položky menu.
        :return: Dvojice obsahující text a metodu pro spuštění akce.
        """
        return (
            f"• {self._menu_items[item_key]['label']}",
            partial(self._response_action, item_key)
        )

    def _response_action(self, item_key: str) -> None:
        """
        Spustí akci odpovídající zvolené položce menu a ukončí aktuální menu.

        Pomocná metody pro metodu get_response_offer(item_key).
        Metoda je v některých třídách přetížena jinou logikou.

        :param item_key: Klíč položky menu, která má být vykonána.
        """
        self.mm.response = item_key
        self.mm.exit_menu()