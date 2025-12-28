"""Tool 'update' command."""

import logging
import shutil


def _find_picto(words, downloads_dir, pictos_dir, pictos_ext):
    """Find and copy a picto to the pictos directory, return picto file name if found."""
    for word in words:
        picto = f"{word}{pictos_ext}"
        src = downloads_dir.joinpath(picto)
        dst = pictos_dir.joinpath(picto)

        if src.is_file():
            if dst.is_file():
                logging.warning("found picto file '%s' in downloads directory, already exists in pictos directory", picto)
            else:
                logging.info("found picto file '%s' in downloads directory, moving to pictos directory", picto)
                shutil.move(src, dst)
            return picto

        if dst.is_file():
            logging.debug("found picto file '%s' in pictos directory", picto)
            return picto


def update(deck, cfg):
    """Tool 'update' command."""
    downloads_dir = cfg.downloads_dir

    # fill in 'picto' field
    pictos_dir = cfg.pictos_dir
    pictos_ext = cfg.pictos_ext

    for card in deck:
        words = [word.strip().lower() for word in card.text.fr.split(",")]

        picto = _find_picto(words, downloads_dir, pictos_dir, pictos_ext)

        if picto:
            if not card.media.picto:
                logging.info("picto file '%s' found, updating picto field", picto)
                card.media.picto = picto
        else:
            if card.media.picto:
                logging.warning("no picto file found for '%s', clearing picto field", card.text.fr)
                card.media.picto = None


    # fill in 'sound' field
    sounds_dir = cfg.sounds_dir
    sounds_ext = cfg.sounds_ext
    sounds_prefix = cfg.sounds_prefix

    # save updated deck
    deck.save()
