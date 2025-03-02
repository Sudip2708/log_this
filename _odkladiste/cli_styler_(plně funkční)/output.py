# cli_styler/output.py
"""
Definuje a vytváří výstupní metody balíčku.
"""
from .cli_styler import CLIStyler

# Vytvoření instance CLIStyler
cs = CLIStyler()

# Nastavení styleru
set_colors_mode = cs.set_colors_mode
set_symbols_mode = cs.set_symbols_mode
get_current_symbols_mode = cs.get_current_symbols_mode
get_current_colors_mode = cs.get_current_colors_mode
get_symbols_modes_dict = cs.get_symbols_modes_dict
get_colors_modes_dict = cs.get_colors_modes_dict


# Vytvoření stylerů

# Prints
print_styled_intro_title = cs.intro_title.style_print
print_styled_intro_end = cs.intro_end.style_print

print_styled_error_title = cs.error_title.style_print
print_styled_error_text = cs.error_text.style_print

print_styled_warning_title = cs.warning_title.style_print
print_styled_warning_text = cs.warning_text.style_print
print_styled_warning_direction = cs.warning_direction.style_print

print_styled_info_title = cs.info_title.style_print
print_styled_info_text = cs.info_text.style_print

print_styled_success_title = cs.success_title.style_print
print_styled_success_text = cs.success_text.style_print

# Styles
get_styled_menu_title = cs.menu_title.style_get
get_styled_menu_offer = cs.menu_offer.style_get
get_styled_menu_selected = cs.menu_selected.style_get

get_styled_hint_title = cs.hint_title.style_get
get_styled_hint_text = cs.hint_text.style_get

get_styled_prompt_input = cs.prompt_input.style_get