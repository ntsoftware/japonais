"""Tool 'copy' command."""

import logging
import shutil


def copy(deck, cfg):
    """Tool 'copy' command."""
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
