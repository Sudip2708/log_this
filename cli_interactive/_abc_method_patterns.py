from .abc_helper import abc_method

# Metoda uzavře aktuální interaktivní menu
exit_menu = abc_method("exit")

# Metoda umožňující ruční zadání int hodnoty (0 - 1000)
input_custom_int_value = abc_method("input_custom_int_value")

# Metoda která vrací data (nadpis a položky) pro konfigurační menu
get_config_menu = abc_method("get_config_menu")

# Metoda která vrací data (položky) pro ukončovací menu
get_ending_menu = abc_method("get_ending_menu")

# Metoda která vrací data (nadpis a položky) pro hlavní menu.
get_main_menu = abc_method("get_main_menu")

# Metoda která na základě 'menu_name' vrátí obsah pro 'menu_title' a 'menu_items'
get_menu_attributes = abc_method("get_menu_attributes")

# Metoda která na základě menu_name vrátí jeho menu_title a menu_items
get_menu_data = abc_method("get_menu_data")

# Metoda která na základě menu_name vrátí jeho menu_title a menu_items
get_menu_items = abc_method("get_menu_items")

# Vrací naformátovaný text pro menu
get_menu_text = abc_method("get_menu_text")

# Metoda která vrací data (nadpis a položky) pro menu pro výběr klíče
get_select_key_menu = abc_method("get_select_key_menu")

# Metoda která vrací data (nadpis a položky) pro menu pro výběr hodnoty pro daný klíč
get_select_value_menu = abc_method("get_select_value_menu")

# Metoda znovu načte data pro vykreselní menu
reload_menu = abc_method("reload_menu")

# Metoda načte a zobrazí aktuální nabídku interaktivního menu
run_menu = abc_method("run_menu")

# Metoda která přepne menu na nové menu
display_menu = abc_method("display_menu")

# Metoda která mění boolean hodnotu atributu 'show_instruction'
toggle_show_instruction = abc_method("show_instructions")