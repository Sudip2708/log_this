from .manager import Manager

# Vytvoření stylerů
cli_styler = Manager()
cli_print = cli_styler.printer
cli_style = cli_styler.styler

# Printy
print_intro_title = cli_print.intro_title
print_intro_end = cli_print.intro_end

print_error_title = cli_print.error_title
print_error_text = cli_print.error_text

print_warning_title = cli_print.warning_title
print_warning_text = cli_print.warning_text
print_warning_direction = cli_print.warning_direction

print_info_title = cli_print.info_title
print_info_text = cli_print.info_text

print_success_title = cli_print.success_title
print_success_text = cli_print.success_text

# Styly
get_menu_title = cli_style.menu_title
get_menu_offer = cli_style.menu_offer
get_menu_selected = cli_style.menu_selected

get_hint_title = cli_style.hint_title
get_hint_offer = cli_style.hint_offer

get_prompt_input = cli_style.prompt_input