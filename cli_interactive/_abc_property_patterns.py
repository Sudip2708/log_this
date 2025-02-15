from .abc_helper import abc_property

# Atribut pro zaznamenání vybrané položky
current_selection = abc_property("current_selection")

# Aplikace s aktuálním menu
interactive_menu = abc_property("interactive_menu")

# Atribut obsahující instanci KeyBindings
kb = abc_property("kb")

# Atribut pro zaznamenání položek zobrazeného menu
menu_items = abc_property("menu_items")

# Atribut pro zaznamenání jaké menu má být zobrazeno
menu_name = abc_property("menu_name")

# Atribut pro zaznamenání nadpisu zobrazeného menu
menu_title = abc_property("menu_title")

# Atribut zaznamenávající požadavek z interaktivního menu
response = abc_property("response")

# Atribut pro zaznamenání vybraného klíče
selected_key = abc_property("selected_key")

# Atribut pro zaznamenání vybrané hodnoty pro daný klíče
selected_value = abc_property("selected_key")

# Atribut pro zaznamenání zda se mají zobrazit instrukce k ovládání
show_instruction = abc_property("show_instruction")
