
def add_show_current_subparser(subparsers):
    """Adds the `interactive` subcommand to the CLI parser."""

    subparsers.add_parser(
        "show-current",
        help="Vypíše aktuální nastavení.",
        description="Umožňuje vypsat aktuální nastavení .",
        epilog="Použijte pro získání aktuálního nastavení.",
        aliases=["s-c", "sc"],
    )


