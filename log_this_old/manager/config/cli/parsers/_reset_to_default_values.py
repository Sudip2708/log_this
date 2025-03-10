
def add_reset_default_subparser(subparsers):
    """Adds the `reset-default` subcommand to the CLI parser."""

    # Setup for the `reset-default` subcommand
    subparsers.add_parser(
        "reset-default",
        help="Resets the configuration.",
        description="Resets the entire configuration to the default state.",
        epilog="",
        aliases=["r-d", "rd"],
    )
