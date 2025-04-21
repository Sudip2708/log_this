from typing import List, Optional, Tuple, Any

from typing import TYPE_CHECKING
if TYPE_CHECKING:  # Importy pro typovou kontrolu
    from ...menus_manager import MenusManager

from ._get_instruction_mixin import GetInstructionMixin
from ._get_menu_title_mixin import GetMenuTitleMixin
from ._get_menu_offer_mixin import GetMenuOfferMixin
# from ._get_instruction_mixin import get_instruction

class GetMenuText(
    GetInstructionMixin,
    GetMenuTitleMixin,
    GetMenuOfferMixin,
):
    """
    Třída definující logiku generování ostylovaného textového menu.

    Mixiny:
        GetInstructionMixin
        # Používá atributy: 'cli', 'lines'
        # Přidává metody:
            _get_instruction() - Zobrazení/skrytí nápovědy.

        GetMenuTitleMixin
        # Používá atributy: 'cli', 'lines'
        # Přidává metody:
            _get_menu_title() - Přidání naformátovaného nadpisu menu.

        GetMenuOfferMixin
        # Používá atributy: 'cli', 'lines',
        # Přidává metody:
            _get_menu_offer() - Přidání naformátované nabídky menu.


    Atributy:
        mm ("MenusManager" | None): Instance správce menu MenusManager.
        lines (List[Any]): Seznam naformátovaného textu menu.
        get_style (callable | None): Metoda vracející tuple se stylem a textem.

    """

    mm: Optional["MenusManager"] = None
    lines: List[Any] = []
    get_style: Any = None

    def __init__(self, menus_manager: "MenusManager") -> None:
        """
        Inicializuje instanci třídy, pokud ještě nebyla inicializována.

        Args:
            menus_manager (object): Správce menu, který obsahuje konfiguraci menu.

        Logika:
            Metoda nejprve zkontroluje, zda již proběhla inicializace.
            Pokud ne, načte instanci MenusManager a přiřadí ji do atributu 'mm',
            a vytvoří atribut definující proběhlou inicializaci.
        """
        if not hasattr(self, "_initialized"):
            self.mm = menus_manager
            self._initialized = True
    #
    def __call__(self) -> List[Tuple[str, str]]:
        """
        Generuje a vrací seznam s naformátovaným textem menu.

        Returns:
            List[Tuple[str, str]]: Seznam obsahující jednotlivé části menu.

        Logika:
        """
        return self._get_instruction() + self._get_menu_offer()


# class GetMenuText:
#
#     def __init__(self, menus_manager: "MenusManager") -> None:
#         if not hasattr(self, "_initialized"):
#             self.mm = menus_manager
#             self._initialized = True
#
#     def __call__(self) -> List[Tuple[str, str]]:
#         lines = []
#         lines.extend(self._get_instruction())
#         lines.extend(self._get_menu_title())  # Přidání nadpisu menu
#         lines.extend(self._get_menu_offer())  # Přidání položek menu
#         return lines