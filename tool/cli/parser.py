"""Tool command-line interface."""

import logging

from argparse import ArgumentParser

from . import command


def parse_args():
    """Parse command-line arguments."""
    parser = ArgumentParser()

    subparsers = parser.add_subparsers(help="command help", required=True)

    parser_check = subparsers.add_parser("check", help="check words list")
    parser_check.add_argument("-v", "--verbose", action="store_true", help="print debug output")
    parser_check.set_defaults(func=command.check)

    parser_copy = subparsers.add_parser("copy", help="copy cards media to anki media collection")
    parser_copy.add_argument("-v", "--verbose", action="store_true", help="print debug output")
    parser_copy.set_defaults(func=command.copy)

    parser_fill = subparsers.add_parser("update", help="fill in words list fields from downloads directory")
    parser_fill.add_argument("-v", "--verbose", action="store_true", help="print debug output")
    parser_fill.set_defaults(func=command.update)

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    return args
