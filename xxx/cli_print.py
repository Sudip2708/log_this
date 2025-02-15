from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text


ANSI_BLUE = "#0000ff"
PASTEL_BLUE = "#0066cc"
DRACULA_BLUE = "#6272a4"
SOLARIZED_BLUE = "#268bd2"


# Definujeme styly
style_dict = {
    "title": f"bold fg:{SOLARIZED_BLUE}",  # Pastelově modrá, tučné
    "default": "fg:default",     # Výchozí nativní barva terminálu
}

def cli_print(style, text):
    """
    Vypíše text s daným stylem, pokud je definován.
    Pokud styl není nalezen, použije výchozí nastavení.

    :param style: Název stylu (např. "title", "default")
    :param text: Řetězec, který se má vypsat
    """
    if style not in style_dict.keys():
        print(text)  # Normální print bez stylu
    else:
        styled_text = FormattedText([("class:" + style, text)])
        custom_style = Style.from_dict(style_dict)
        print_formatted_text(styled_text, style=custom_style)
