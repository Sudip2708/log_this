# print("_response_manager/_print_configuration.py")
from cli_styler import cli_print

def print_configuration():
    cli_print.success.title("Aktuální konfigurace:")
    cli_print.success.text("key1: value1")
    cli_print.success.text("key2: value2")
    print()

