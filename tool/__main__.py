"""Words list tool."""

import logging

from . import cli, config, model


def main():
    """Tool entry point."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    cfg = config.load("tool.ini")

    deck = model.deck.load(cfg)

    args = cli.parse_args()
    args.func(deck, cfg)


if __name__ == "__main__":
    main()
