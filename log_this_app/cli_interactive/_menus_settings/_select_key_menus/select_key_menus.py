from ._select_key_menu import SelectKeyMenu


class SelectKeyMenuInteractive(SelectKeyMenu):
    """
    Menu pro výběr klíče pro nastavení vzhledu interaktivního režimu.

    Umožňuje přístup k možnostem pro změnu vzhledu CLI
    prostřednictvím výběru přednastavených stylů.
    """
    menu_name: str = "Menu pro nastavení vzhledu interaktivního režimu"
    _menu_key: str = "select_key_menu_interactive"
    _previous_menu_key: str = "main_menu"
    _category: str = "interactive_cli"
    _next_menu: str = "select_value_menu_interactive"


class SelectKeyMenuModes(SelectKeyMenu):
    """
    Menu pro výběr klíče pro nastavení módů logování.

    Poskytuje přístup k možnostem změny úrovní a režimů logování aplikace.
    """

    menu_name: str = "Menu pro nastavení módů logování"
    _menu_key: str = "select_key_menu_modes"
    _previous_menu_key: str = "main_menu"
    _category: str = "log_this_modes"
    _next_menu: str = "select_value_menu_modes"


class SelectKeyMenuAspects(SelectKeyMenu):
    """
    Menu pro výběr klíče pro nastavení aspektů logování.

    Umožňuje přístup k možnostem pro výběr specifických parametrů logování.
    """

    menu_name: str = "Menu pro nastavení aspektů logování"
    _menu_key: str = "select_key_menu_aspects"
    _previous_menu_key: str = "main_menu"
    _category: str = "log_this_aspects"
    _next_menu: str = "select_value_menu_aspects"