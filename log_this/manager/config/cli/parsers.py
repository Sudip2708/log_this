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


    # Setup for the `show` subcommand
    subparsers.add_parser(
        "show",
        help="Displays the current configuration.",
        description="Allows displaying the currently used configuration.",
        epilog="Primarily used to get an overview of set values or to check for changes.",
        aliases=["s"],
    )


    # Setup for the `set` subcommand
    set_parser = subparsers.add_parser(
        "set",
        help="Sets the value of a key.",
        description="Allows changing the value of specific configuration keys.",
        epilog="Used for making a specific change to a configuration key.",
        aliases=["i"],
    )
    # Argument for specifying the key
    set_parser.add_argument(
        "--key", "-k",
        required=True,
        help="Configuration key.",
        choices=list(config.DEFAULTS.keys()),
        metavar='NAME OF KEY'
    )
    # Argument for specifying the value
    set_parser.add_argument(
        "--value", "-v",
        required=True,
        help="Value of the key.",
        metavar='VALUE'
    )


    # Setup for the `reset` subcommand
    subparsers.add_parser(
        "reset",
        help="Resets the configuration.",
        description="Resets the entire configuration to the default state.",
        epilog="This command will permanently delete all changes.",
        aliases=["r"],
    )


    # Setup for the `export` subcommand
    export_parser = subparsers.add_parser(
        "export",
        help="Exports the configuration to a file.",
        description="Allows saving the configuration to an external file.",
        epilog="Used for backup or transferring configuration.",
        aliases=["e"],
    )
    # Argument for specifying the output file path
    export_parser.add_argument(
        "--file-path", "--file", "-f",
        required=True,
        help="Path to the output file.",
        metavar='FILEPATH'
    )


    # Setup for the `import` subcommand
    import_parser = subparsers.add_parser(
        "import",
        help="Loads the configuration from a file.",
        description="Allows using configuration from an external file.",
        epilog="Used for quickly adjusting the configuration from a custom config file.",
        aliases=["i"],
    )
    # Argument for specifying the input file path
    import_parser.add_argument(
        "--file-path", "--file", "-f",
        required=True,
        help="Path to the input file.",
        metavar='FILEPATH'
    )

    return parser
