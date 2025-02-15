from .setup_key_bindings import SetupKeyBindingsMixin

__all__ = [
    "SetupKeyBindingsMixin",  # setup_key_bindings()
    # Nastavení klávesových příkazů pro používání interaktivního menu
    # Používá atributy: 'kb', 'current_selection', 'menu_items'
    # Používá metodu: reload_menu(), exit_menu()
]