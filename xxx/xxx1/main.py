from menu_view import MenuView
from menu_controller import MenuController
from key_bindings import MenuKeyBindings
from config import Config

def main():
    print("Vítejte v interaktivním režimu:")
    print("--------------------------------")

    config = Config()
    while True:
        view = MenuView(None, None)  # Dočasné None hodnoty
        view.controller = MenuController(view, config)
        key_bindings = MenuKeyBindings(view.controller)
        view.main_content.key_bindings = key_bindings.get_bindings()

        view.run()
        if not view.controller.menu_items[view.controller.current_selection][
                   0] == "Ukončit":
            continue
        else:
            print("Ukončuji interaktivní režim...")
            break


if __name__ == "__main__":
    main()