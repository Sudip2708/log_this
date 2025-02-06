from log_this.manager.config.keys import allowed_keys_with_descriptions

def add_set_subparser(subparsers):
    """Adds the `set` subcommand to the CLI parser."""

    set_parser = subparsers.add_parser(
        "set",
        help="Sets the value of a key.",
        description="Allows changing the value of specific configuration keys.",
        epilog="Used for making a specific change to a configuration key.",
        aliases=["s"],
    )

    # Poziční argument pro klíč
    set_parser.add_argument(
        "key",
        help="Configuration key.",
        choices=allowed_keys_with_descriptions(),
        metavar="KEY"
    )

    # Volitelný poziční argument "to" (jen pro čitelnost)
    set_parser.add_argument(
        "to",
        help="Literal 'to'. For readability.",
        choices=["to"],
        metavar="'to'",
        nargs="?"
    )

    # Poziční argument pro hodnotu
    set_parser.add_argument(
        "value",
        help="Value to set for the key.",
        metavar="VALUE"
    )
