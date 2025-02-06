
def add_interactive_subparser(subparsers):
    """Adds the `interactive` subcommand to the CLI parser."""

    subparsers.add_parser(
        "interactive",
        help="Spustí interaktivní režim.",
        description="Umožňuje přístup ke konfiguraci interaktivní bezpečnou cestou.",
        epilog="Použijte tento přístup pro změnu konfigurace a ostatní úkony dle předem specifikovaných kroků.",
        aliases=["i"],
    )

