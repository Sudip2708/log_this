from cli_styler import cli_print, SUCCESS, LIST, END_LINE, EMPTY_LINE

def print_configuration():
    title = "Aktuální konfigurace:"
    cli_print([
        ("success.title", f"{SUCCESS}{title}{END_LINE}"),
        ("success.text", f"{LIST}key1: value1{END_LINE}"),
        ("success.text", f"{LIST}key2: value2{END_LINE}"),
        ("default", f"{EMPTY_LINE}")
    ])
