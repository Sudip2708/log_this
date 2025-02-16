from cli_styler import cli_style, cli_print

def print_configuration():
    cli_print("cli_success.title", " ☑ Aktuální konfigurace:")
    cli_print("cli_success.text", " - key1: value1")
    cli_print("cli_success.text", " - key2: value2")
    print()
