from .cli_styler import CLIStyler

# Vytvoření instance CLIStyler
cs = CLIStyler()

# Vytvoření stylerů

# Printy
print_intro_title = cs.intro_title.print_styled
print_intro_end = cs.intro_end.print_styled

print_error_title = cs.error_title.print_styled
print_error_text = cs.error_text.print_styled

print_warning_title = cs.warning_title.print_styled
print_warning_text = cs.warning_text.print_styled
print_warning_direction = cs.warning_direction.print_styled

print_info_title = cs.info_title.print_styled
print_info_text = cs.info_text.print_styled

print_success_title = cs.success_title.print_styled
print_success_text = cs.success_text.print_styled

# Styly
get_menu_title = cs.menu_title.get_styled
get_menu_offer = cs.menu_offer.get_styled
get_menu_selected = cs.menu_selected.get_styled

get_hint_title = cs.hint_title.get_styled
get_hint_offer = cs.hint_offer.get_styled

get_prompt_input = cs.prompt_input.get_styled