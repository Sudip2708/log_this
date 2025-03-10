import argparse

def create_parser():
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

    return parser, subparsers  # Vrací parser i subparsers pro další rozšíření
