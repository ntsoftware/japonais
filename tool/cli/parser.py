"""Tool command-line interface."""

import logging

from argparse import ArgumentParser

from . import command


def parse_args():
    """Parse command-line arguments."""
    parser = ArgumentParser()

    subparsers = parser.add_subparsers(help="command help", required=True)

    parser_fill = subparsers.add_parser("update", help="fill in missing fields in words list")
    parser_fill.add_argument("-v", "--verbose", action="store_true", help="print debug output")
    parser_fill.set_defaults(func=command.update)

    parser_sync = subparsers.add_parser("sync", help="copy cards media to anki media collection")
    parser_sync.add_argument("-v", "--verbose", action="store_true", help="print debug output")
    parser_sync.set_defaults(func=command.sync)

    parser_forvo = subparsers.add_parser("forvo", help="download sounds from the forvo pronunciations dictionary")
    parser_forvo.add_argument("-v", "--verbose", action="store_true", help="print debug output")
    parser_forvo.add_argument("words", nargs="+", help="words to look-up")
    parser_forvo.set_defaults(func=command.forvo)

    parser_ojad = subparsers.add_parser("ojad", help="look-up words in the Online Japanese Accent Dictionary")
    parser_ojad.add_argument("-v", "--verbose", action="store_true", help="print debug output")
    parser_ojad.add_argument("words", nargs="+", help="words to look-up")
    parser_ojad.set_defaults(func=command.ojad)

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    return args
