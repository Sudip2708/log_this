from .signs import INFO, END_LINE, LIST, EMPTY_LINE, DROPDOWN, SELECTED, UNSELECTED

LAVENDER = "#d19bfe"
PINK = "#d270ba"
MAGENTA = "#c95fbb"
DARK_GREEN = "#4f9d4f"
GREEN = "#178f17"
LIGHT_GREEN = "#66cc66"


# Styly pro cli_style
DIALOG_STYLES = {

    # Interaktivní menu
    "menu": "noinherit",  # Zamezí dědění globálních stylů
    "menu.title": f"{DARK_GREEN} bold reverse",
    "menu.focus": f"{GREEN} bold reverse",
    "menu.offer": f"{LIGHT_GREEN}",

    # Nápověda k ovládání interaktivního režimu
    "hint.title": f"{PINK} bold reverse",
    "hint.offer": f"{MAGENTA}",

    # Styl pro prompt() pro zadání hodnoty
    "prompt": f"{LAVENDER} bold",

}

def get_menu_title(title):
    return "class:menu.title", f"{DROPDOWN}{title}{END_LINE}"

def get_menu_selected_offer(text):
    return "class:menu.focus", f"{SELECTED}{text}{END_LINE}"

def get_menu_offer(text):
    return "class:menu.offer", f"{UNSELECTED}{text}{END_LINE}"

def set_hint_title(title):
    return "class:hint.title", f"{INFO}{title}{END_LINE}"

def set_hint_offer(text):
    return "class:hint.offer", f"{LIST}{text}{END_LINE}"

def set_empty_line():
    return "class:", f"{EMPTY_LINE}"


def get_menu_title(title):
    style = f"{DARK_GREEN} bold reverse"
    text = f"{DROPDOWN}{title}{END_LINE}"
    return style, text

LIGHT_THEME = {
    "menu.title": "green bold",
    "menu.focus": "blue reverse",
    "menu.offer": "lightgreen",
}

DARK_THEME = {
    "menu.title": "cyan bold",
    "menu.focus": "magenta reverse",
    "menu.offer": "yellow",
}

USE_DARK_THEME = True

def set_menu_title(title):
    theme = DARK_THEME if USE_DARK_THEME else LIGHT_THEME
    return theme["menu.title"], f"{DROPDOWN}{title}{END_LINE}"
