
def add_examples_subparser(subparsers):
    """Adds the `interactive` subcommand to the CLI parser."""

    interactive_parser = subparsers.add_parser(
        "examples",
        help="Spustí interaktivní režim s příklady použití.",
        description="Dává nahlídnout do toho, jak knihovnu správně používat.",
        epilog="Použijte tuto možnost když se chcete podívat na interaktivní příklady použití.",
        aliases=["exa"],
    )

