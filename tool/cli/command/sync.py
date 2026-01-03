"""Tool 'sync' command."""

import logging
import shutil

from tool import config, model


def sync(_args):
    """Tool 'sync' command."""

    cfg = config.load()

    deck = model.deck.load(cfg)

    media_dir = cfg.anki_path.joinpath(cfg.anki_user, "collection.media")

    for card in deck:
        picto = card.media.picto
        if picto:
            src = cfg.pictos_dir.joinpath(picto)
            dst = media_dir.joinpath(picto)
            if not dst.is_file():
                logging.info("copy picto file '%s' to anki media directory", picto)
                shutil.copy(src, dst)

        sound = card.media.sound
        if sound:
            src = cfg.sounds_dir.joinpath(sound)
            dst = media_dir.joinpath(sound)
            if not dst.is_file():
                logging.info("copy sound file '%s' to anki media directory", sound)
                shutil.copy(src, dst)
