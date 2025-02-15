from .abc_helper import abc_property, abc_method

### Atribiutes:

# Atribut pro zaznamenání nadpisu zobrazeného menu
menu_title = abc_property("menu_title")

# Atribut pro zaznamenání položek zobrazeného menu
menu_items = abc_property("menu_items")

# Atribut pro zaznamenání jaké menu má být zobrazeno
menu_name = abc_property("menu_name")

# Atribut pro zaznamenání zda se mají zobrazit instrukce k ovládání
show_instruction = abc_property("show_instruction")



### Methods:

# Metoda která na základě menu_name vrátí jeho menu_title a menu_items
get_menu_items = abc_method("get_menu_items", "menu_name")

# Metoda která mění boolean hodnotu atributu 'show_instruction'
toggle_show_instruction = abc_method("show_instructions")