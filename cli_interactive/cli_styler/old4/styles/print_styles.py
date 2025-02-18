BLUE = "#268bd2"
LIGHT_PURPLE = "#bf7fff"
PURPLE = "#ab72dc"
BROWN = "#bb8940"
ORANGE = "#f7a734"
RED = "#bb4040"
LIGHT_RED = "#e76b6b"


# Styly pro cli_print()
PRINT_STYLES = {

    # Nastavení na nativní styl terminálu
    "default": "default",

    # Úvodní oznam a ukončení aplikace
    "intro.title": f"{BLUE} bold reverse",
    "intro.end": f"{BLUE}",

    # Výpis chyb
    "error.title": f"{LIGHT_RED} bold reverse",
    "error.text": f"{RED}",


    # Oznamy
    "info.title": f"{LIGHT_PURPLE} bold reverse",
    "info.text": f"{PURPLE}",

    # Výstup
    "success.title": f"{BROWN} bold reverse",
    "success.text": f"{ORANGE}",

}