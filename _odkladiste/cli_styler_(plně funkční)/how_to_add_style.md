Jak přidat nový styl

1) V balíčku "styles_settings" vytvořte nový python soubor jehož název začíná pomlčkou a pokračuje názvem stylu.
2) Způcob zápisu stylu je následující:

STYLE_NAME = {
    "symbol": SYMBOL_CONSTANT,
    "color": COLOR_CONSTANT,
    "style": STYLE_CONSTANT,
    "end_line": END_LINE_CONSTANT
}

Popis jednotlivých částí kodu:
STYLE_NAME: Název stylu by měl popisovat použití
"symbol": Klíč pro značkou která je uvedena na začátku řádku
"color": Klíč pro nastavení barva textu
"style": Klíč pro doplňujcí stylování textu
"end_line": Klíč pro zakončení řádku
SYMBOL_CONSTANT: Konstanty obsahující seznam se sadami symbolů
COLOR_CONSTANT: Konstanty obsahující seznam se sadami barev
STYLE_CONSTANT: Konstanty pro doplňijící stylizaci textu
END_LINE_CONSTANT: Konstanty pro zakončení řádku
(Všechny konstanty odkazují na předpřipravené řetězce obsahující daný kod.)

Konstanty momentálně obsahují tyto možnosti:
SYMBOLS_CONSTANT:
INTRO        = [" ■ ", " 🟢 "]
INFO         = [" ☐ ", " ℹ️ "]
LIST         = [" - ", " • "]
SUCCESS      = [" ☑ ", " ✔️ "]
DROPDOWN     = [" ▼ ", " 🔽 "]
SELECTED     = [" » ", " ▶️ "]
UNSELECTED   = ["   ", "   "]
ERROR        = [" ⛝ ", " ❌ "]
WARNING      = [" ⚠ ", " ⚠️ "]
NO_SIGN      = ["", ""]

COLORS_CONSTANT:
LAVENDER     = ["#d19bfe", "#b77fdc"]
PINK         = ["#d270ba", "#b85a9e"]
MAGENTA      = ["#c95fbb", "#af4aa0"]
DARK_GREEN   = ["#4f9d4f", "#3e7f3e"]
GREEN        = ["#178f17", "#127112"]
LIGHT_GREEN  = ["#66cc66", "#53a653"]
BLUE         = ["#268bd2", "#1f72ad"]
LIGHT_PURPLE = ["#bf7fff", "#a56cdc"]
PURPLE       = ["#ab72dc", "#905fbb"]
BROWN        = ["#bb8940", "#9c7134"]
ORANGE       = ["#f7a734", "#d08b2b"]
RED          = ["#bb4040", "#9c3434"]
LIGHT_RED    = ["#e76b6b", "#c05a5a"]

STYLES_CONSTANT:
NONE         = ""
BOLD         = " bold"
BOLD_REVERSE = " bold reverse"

ENDS_CONSTANT:
END_LINE     = " \n"
EMPTY_LINE   = "\n"
CONTINUE     = ""

Všechny konstanty jsou přístupné přes balíček. 
Pro jejich načtení tedy stačí zadat:

from ..constants import CONSTANT_NAME

V jednom souboru můžete definovat více nastavení. Například pro nadpis a pro text.
Každé nastavení musí být samostatnou položkou obsahující hodnoty pro všechny uvedené klíče.

Zde je pro ukázku kodu pro nastavení chybových oznamů:

# cli_styler/styles/_error.py
"""
Definice stylů pro oznamy chyb
ERROR_TITLE: Nadpis
ERROR_TEXT: Položky textu
"""
from ..constants import (
    ERROR, LIST,
    LIGHT_RED, RED,
    BOLD_REVERSE, NONE,
    END_LINE
)
ERROR_TITLE = {
    "symbol": ERROR,
    "color": LIGHT_RED,
    "style": BOLD_REVERSE,
    "end_line": END_LINE
}
ERROR_TEXT = {
    "symbol": LIST,
    "color": RED,
    "style": NONE,
    "end_line": END_LINE
}

Po definici stylu je potřeba styl přidat do slovníku STYLES_DICT, 
který je hlavním výstupním slovníkem všech zde definovaných stylů:

# cli_styler/styles/styles_dict.py

Styl je potřeba nejprve importovat a po té pro něj vytvořit klíč 
opysující název stylu a odkazující na daný styl.
Klíč je malým písmem a styl velkými.

from ._style_name import STYLE_NAME_PART
STYLES_DICT = {
   ...
   "style_name_part"     : STYLE_NAME_PART,
}

Zde je pro ukázku kod pro přidání chybových oznamů:

    "error_title"       : ERROR_TITLE,
    "error_text"        : ERROR_TEXT,

Tím je styl přístupná přes slovník stylů STYLES_DICT.
Pro to aby bylo možné styl i používat je potřeba ho ještě i zaregistrovat 
jako atribut na hlavní třídě CLIStyler:

# cli_styler/cli_styler.py
class CLIStyler(...):
    style_name_part = None

Důležité je aby se název atributu shodoval s názvem klíče 
ve slovníku STYLES_DICT, který odkazuje na slovník stylu.

Atribut by měl být nastaven na hodnotu None 
a bude přepsán při inicializaci nebo změně stylu 
na aktuální hodnoty dle zvoleného nastavení.

Zde je pro ukázku kod pro přidání chybových oznamů:

    # Chybové oznamy
    error_title = None
    error_text = None

Tím se stává styl přístupný přes instanci třídy CLIStyler,
a pokud nám stačí přístup k němu přes instanci třídy máme hotovo.

Volitelně je možné předat styl jako metodu 
vracející slovník obsahující řetězce pro styl a text, 
nebo metodu vypysující ostylovaný text do konzole.

K tomuto účelu slouží soubor output.py, kde je možné definovat 
výstupní metodu prostřednictvím instance.
# cli_styler/output.py

Metody jsou zde řazeny do dvou skupin Prints a Styles.

Formát pro tvoření názvu metod:

# Prints
...
print_styled_style_name_part = cs.style_name_part.style_print
# Styles
...
get_style_name_part = cs.style_name_part.style_get

Zde je pro ukázku kod pro přidání chybových oznamů:

print_styled_error_title = cs.error_title.style_print
print_styled_error_text = cs.error_text.style_print

Posledním krokem je zpřístupnit metodu prostředníctvím souboru __init__.py celého balíčku:
# cli_styler/__init__.py

Metodu je nejprve potřeba importovat. 
Momentální styl je na jeden řádek všechny varianty jednoho názvu stylu,
děleno do sekcí get a print.

Samotnou metodu pak ještě vloříme jako řetězec do seznamu __all__

__all__ = [
    ...
    "print_styled_style_name_part",
    "get_styled_style_name_part"
]

Zde je pro ukázku kod pro přidání chybových oznamů:

    # Styler pro chybové oznamy (tiskne nastylovaný text)
    "print_styled_error_title",  # Nadpis chybového oznamu
    "print_styled_error_text",  # Položka chybového oznamu

Po těchto úpravách je pak možné danou metodu načíst prostřednictvím balíčku cli_styler:
from cli_styler import print_styled_style_name_part, get_styled_style_name_part

A používat ji výpis do konzole:
print_styled_style_name_part("text_to_be_styled")

Nebo pro získání tuple se stylem a upraveným textem 
a používat například pro definici dialogových nabýdek:

style, formatted_text = get_style_name_part("text_to_be_styled")
input = prompt(
    formatted_text,
    style = style
)