
def add_help_subparser(subparsers):
    """Adds the `interactive` subcommand to the CLI parser."""

    help_parser = subparsers.add_parser(
        "help",
        help="Spustí interaktivní nápovědu.",
        description="Umožňuje přístup k nápovědě prostřednictvím interaktivního režimu.",
        epilog="Použijte pro získání nápovědy a ukázek, jak s knihovnou pracovat.",
        aliases=["h"],
    )

