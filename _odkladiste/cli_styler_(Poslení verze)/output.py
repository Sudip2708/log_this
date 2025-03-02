# cli_styler/output.py
"""
Definuje a vytváří výstupní metody balíčku.
"""
from .style_manager import styler, cli_style, cli_print

# Nastavení styleru
# set_colors_mode = cs.set_colors_mode
# set_symbols_mode = cs.set_symbols_mode
# get_current_symbols_mode = cs.get_current_symbols_mode
# get_current_colors_mode = cs.get_current_colors_mode
# get_symbols_modes_dict = cs.get_symbols_modes_dict
# get_colors_modes_dict = cs.get_colors_modes_dict


# Vytvoření stylerů

# Prints
print_styled_intro_title = cli_print.intro.title
print_styled_intro_end = cli_print.intro.end

print_styled_error_title = cli_print.error.title
print_styled_error_text = cli_print.error.text

print_styled_warning_title = cli_print.warning.title
print_styled_warning_text = cli_print.warning.text
print_styled_warning_direction = cli_print.warning.direction

print_styled_info_title = cli_print.info.title
print_styled_info_text = cli_print.info.text

print_styled_success_title = cli_print.success.title
print_styled_success_text = cli_print.success.text

# Styles
get_styled_menu_title = cli_style.menu.title
get_styled_menu_offer = cli_style.menu.offer
get_styled_menu_selected = cli_style.menu.selected

get_styled_hint_title = cli_style.hint.title
get_styled_hint_text = cli_style.hint.text

get_styled_prompt_input = cli_style.prompt.input