# print("_response_manager/_print_new_settings.py")
from cli_styler import cli_print


def print_new_settings(cli):
    """Tiskne aktuálně změněnou hodnotu"""
    cli_print.success.title(
        f"Vybrán klíč: {cli.selected_key}, "
        f"hodnota: {cli.selected_value}"
    )
    print()
    cli.selected_key = None
    cli.selected_value = None