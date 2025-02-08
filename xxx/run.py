from interactive_main_menu import ImprovedInlineMenu
from print_response import PrintResponse
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText



if __name__ == "__main__":

    # style = Style.from_dict({
    #     'title': 'yellow',
    # })
    #
    # print_formatted_text(
    #     FormattedText([
    #         ('class:title', '\nVítejte v ineraktivním režimu:\n--------------------------------')
    #     ]), style=style)


    print()
    print("Vítejte v ineraktivním režimu:")
    print("--------------------------------")
    while True:
        ImprovedInlineMenu(menu_type="main").run()
        if PrintResponse.response:
            PrintResponse.print_response()
        else:
            print("Ukončuji interaktivní režim...")
            break