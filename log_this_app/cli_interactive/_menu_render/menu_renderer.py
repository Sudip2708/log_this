from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout, HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from typing import TYPE_CHECKING
from typing import List, Optional, Tuple, Any
# Importy pro typovou kontrolu:
if TYPE_CHECKING:
    from ..menus_manager import MenusManager
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from ._run_methods_mixins import RunMethodsMixin
from cli_styler import styler

class MenuRenderer(RunMethodsMixin):

    # Instance CLI aplikace.
    menu_app: Application | None = None

    def __init__(self, menus_manager: "MenusManager") -> None:
        """
        Inicializuje renderer menu a nastaví klávesové zkratky i text menu.

        Args:
            menus_manager (object): Správce menu, který obsahuje informace o menu.

        Atributy:
            kb (KeyBindingsManager): Správce klávesových zkratek.
            get_menu_text (GetMenuText): Generátor textového obsahu menu.
            menu_app (Application | None): Instance CLI aplikace.
        """
        self._menus_manager = menus_manager
        self._key_bindings = self._get_key_bindings()
        self.menu_app = self.create_menu_app()

    def create_menu_app(self) -> Application:
        main_content = FormattedTextControl(
            text=self._get_menu_text,  # Načtení textu
            key_bindings=self._key_bindings,  # Načtení klávesových ovladačů
            focusable=True,
            show_cursor=False
        )

        layout = Layout(
            HSplit([
                Window(content=main_content)
            ])
        )

        return Application(
            layout=layout,
            full_screen=False,
            erase_when_done=False
        )


    def _get_menu_text(self) -> List[Tuple[str, str]]:
        menu = self._menus_manager.current_menu
        return self._get_instruction(menu) + self._get_menu_offer(menu)


    def _get_menu_offer(self, menu):

        style = styler.get_style.menu
        selected_line_id = self._menus_manager.selected_item_id 

        return [

            # Nadpis
            style.title(menu.title) if menu.title else "",

            # Položky
            *[
                style.selected(text)
                if i == selected_line_id else style.offer(text)
                for i, (text, _) in enumerate(menu.items)
            ]
        ]

    def _get_instruction(self, menu):
        if not self._menus_manager.show_instruction:
            return []

        last_item_id = len(menu.menu_help) - 1
        style = styler.get_style.hint

        return [

            # Instrukce k ovládání
            style.title("NÁPOVĚDA:"),
            style.text("Použijte šipky ↑↓ pro výběr položky"),
            style.text("Stiskněte Enter pro potvrzení výběru"),
            style.text("Ctrl+C pro ukončení\n"),

            # Nadpis nápovědy
            style.title(f"Popis položek pro {menu.menu_name.lower()}:"),

            # Položky nápovědy
            *[
                style.text(text if index != last_item_id else text + "\n")
                for index, text in enumerate(menu.menu_help)
            ]
        ]

    def _get_key_bindings(self):

        key_bindings = KeyBindings()

        @key_bindings.add("up")
        def handle_up(event: KeyPressEvent) -> None:
            """Přesune výběr v menu nahoru."""
            self._menus_manager.go_up()

        @key_bindings.add("down")
        def handle_down(event: KeyPressEvent) -> None:
            """Přesune výběr v menu dolů."""
            self._menus_manager.go_down()

        @key_bindings.add("enter")
        def handle_enter(event: KeyPressEvent) -> None:
            """Potvrdí aktuálně vybranou možnost v menu."""
            self._menus_manager.run_selected_item_id ()

        @key_bindings.add("c-c")
        def handle_ctrl_c(event: KeyPressEvent) -> None:
            """Ukončí menu při stisknutí Ctrl+C."""
            self._menus_manager.exit_menu()

        return key_bindings
