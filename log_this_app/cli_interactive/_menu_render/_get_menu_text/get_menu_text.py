# print("_menu_render/_get_menu_text/get_menu_text.py")
from ._get_instruction_mixin import GetInstructionMixin
from ._get_menu_title_mixin import GetMenuTitleMixin
from ._get_menu_offer_mixin import GetMenuOfferMixin

class GetMenuText(

    GetInstructionMixin,
    # Mixin přidávající metodu pro zobrazení/skrytí nápovědy
    # Přidává metody: _get_instruction()
    # Používá atributy: 'cli', 'lines'

    GetMenuTitleMixin,
    # Mixin přidávající metodu pro přidání naformátovaného nadpisu menu
    # Přidává metody: _get_menu_title()
    # Používá atributy: 'cli', 'lines'

    GetMenuOfferMixin,
    # Mixin přidávající metodu pro přidání naformátované nabídky menu
    # Přidává metody: _get_menu_offer()
    # Používá atributy: 'cli', 'lines',

):
    """Třída definující logiku navracející seznam s položkami ostylovaného menu"""

    # Atributy použité v mixinech
    lines = []  # Atribut pro seznam s naformátovaným textem
    mm = None  # Atribut pro přístup k instanci InteractiveCli
    get_style = None  # Atribut s metodou navrácející tuple se stylem a textem

    def __init__(self, menus_manager):
        """Inicializační metoda singleton instance"""

        # Kontrola zda již proběhla inicializace
        if not hasattr(self, "_initialized"):

            # Načtení instance hlvní třídy
            self.mm = menus_manager

            # Potvrzení o proběhlé inicializaci
            self._initialized = True


    def __call__(self):
        """Vrací naformátovaný text pro zobrazení menu"""

        # Vyčištění obsahu atributu lines
        self.lines = []

        # Zobrazení nápovědy (je-li aktivní)
        self._get_instruction()

        # Přidání nadpisu (je-li)
        self._get_menu_title()

        # Přidání položek menu
        self._get_menu_offer()

        # Vrácení seznamu s tuple obsahující naformátovaný text pro menu
        output = self.lines
        # print("### output: ", output)

        return output
