from cli_styler import cli_print


# print("_response_manager/_input_int_value/_result_processing.py")
def result_processing(selected_value, cli):

    # Pokud je výsledek
    if selected_value:

        # Nastaví atributu 'selected_value' na danou hodnotu
        cli.selected_value = selected_value

        # Nastaví atributu 'response' na vytištění výsledku
        cli.response = "print_new"

    # Pokud nebyla zadaná žádná hodnota (pro opuštění zadání)
    else:

        # Vypíše se oznam o návratu do menu pro výběr hodnoty
        cli_print.warning.title("Nebyla zadaná žádná hodnota.")
        cli_print.warning.direction("Návrat do menu pro výběr hodnoty.")

        # Vyčistí se obsah atributu 'response'
        cli.response = None

        # Načtení a spuštění okna s menu pro výběr hodnoty
        cli.switch_menu("select_value_menu")
        cli.run_menu()