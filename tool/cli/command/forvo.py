"""Tool 'forvo' command."""

from tool import config
from tool.service.forvo import download_pronunciations


def forvo(args):
    """Tool 'forvo' command."""

    cfg = config.load()

    for word in args.words:
        download_pronunciations(word, cfg.forvo_cookie, cfg.sounds_dir)
