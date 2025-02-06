
def add_import_subparser(subparsers):
    """Adds the `interactive` subcommand to the CLI parser."""

    # Setup for the `import` subcommand
    import_parser = subparsers.add_parser(
        "import",
        help="Loads the configuration from a file.",
        description="Allows using configuration from an external file.",
        epilog="Used for quickly adjusting the configuration from a custom config file.",
        aliases=["imp"],
    )

    # Argument for specifying the input file path
    import_parser.add_argument(
        "file", "file-path", "f",
        required=True,
        help="Path to the input file.",
        metavar='FILEPATH'
    )
