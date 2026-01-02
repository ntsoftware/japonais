"""Words list tool."""

import logging

from . import cli


def main():
    """Tool entry point."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    args = cli.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
