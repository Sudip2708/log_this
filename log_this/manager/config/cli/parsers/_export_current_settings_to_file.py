
def add_export_subparser(subparsers):
    """Adds the `interactive` subcommand to the CLI parser."""

    # Setup for the `export` subcommand
    export_parser = subparsers.add_parser(
        "export",
        help="Exports the configuration to a file.",
        description="Allows saving the configuration to an external file.",
        epilog="Used for backup or transferring configuration.",
        aliases=["exp"],
    )

    # Argument for specifying the output file path
    export_parser.add_argument(
        "file", "file-path", "f",
        required=True,
        help="Path to the output file.",
        metavar='FILEPATH'
    )


