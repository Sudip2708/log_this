# cli_styler/utils/_raise_attributes_error.py

def raise_attributes_error(attributes_set, styles_set):
    """
    Funkce vytvoří chybový oznam a po té vyvolá výjimku

    Funkce je určená pro metodu třídy CLIStyler:
    _check_style_attributes(self, styles_dict)

    Očekává validní data, která již dále nevaliduje.
    """

    # Úvodní oznam
    message = "Neshoda mezi definovanými styly a atributy třídy CLIStyler\n"

    # Přidání oznamu o atributech,
    # které jsou definované na třídě,  ale ve slovníku chybý
    excess = attributes_set - styles_set
    message += f"Nadytečné atributy třídy CLIStyler: {excess}\n" \
        if excess else ""

    # Přidání oznamu o atributech,
    # které jsou definované ve slovníku, ale na třídě  chybý
    missing = styles_set - attributes_set
    message += f"Chybějící atributy třídy CLIStyler: {missing}\n" \
        if missing else ""

    # Volání výjimky
    raise ValueError(message)