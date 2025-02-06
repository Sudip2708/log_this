
def add_reset_previous_subparser(subparsers):
    """Adds the `reset-previous` subcommand to the CLI parser."""

    # Setup for the `reset-previous` subcommand
    subparsers.add_parser(
        "reset-previous",
        help="Resets to the previous configuration.",
        description="Resets the entire configuration to the previous state.",
        epilog="",
        aliases=["r-p", "rp"],
    )
