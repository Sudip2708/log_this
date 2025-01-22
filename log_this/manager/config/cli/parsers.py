# log_this/manager/config/cli/parsers.py
import argparse


def create_parser(config):
    """Creates the main parser and subparsers."""

    # Main parser setup
    parser = argparse.ArgumentParser(
        description="Tool for managing the configuration of the log_this library.",
        epilog="Thank you for using our tool!",
        prog="log-this-config"
    )

    # Subparser setup
    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    # Setup for the `set` subcommand
    set_parser = subparsers.add_parser(
        "set",
        help="Sets the value of a key.",
        description="Allows changing the value of specific configuration keys.",
        epilog="Used for making a specific change to a configuration key.",
        aliases=["i"],
    )
    # Poziční argument pro klíč
    set_parser.add_argument(
        "key",
        help="Configuration key.",
        choices=list(config.DEFAULTS.keys()),
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

    return parser
