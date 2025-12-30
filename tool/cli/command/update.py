"""Tool 'update' command."""

import logging
import shutil


def _find_picto(card, downloads_dir, pictos_dir, pictos_ext):
    """Find and copy a picto to the pictos directory, return picto file name if found."""

    words = [word.strip().lower() for word in card.text.fr.split(",")]

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


def _update_pictos(deck, cfg):
    """Update picto field of all cards in the deck."""

    downloads_dir = cfg.downloads_dir
    pictos_dir = cfg.pictos_dir
    pictos_ext = cfg.pictos_ext

    for card in deck:
        if card.has_picto(pictos_dir):
            continue

        picto = _find_picto(card, downloads_dir, pictos_dir, pictos_ext)

        if picto:
            if not card.media.picto:
                logging.info("picto file '%s' found, updating picto field", picto)
                card.media.picto = picto
        else:
            if card.media.picto:
                logging.warning("no picto file found for '%s', clearing picto field", str(card))
                card.media.picto = None


def _find_sound(card, downloads_dir, sounds_dir, sounds_ext, sounds_prefix):
    """TODO"""

    words = [word.strip().lower() for word in (card.text.ja, card.text.furigana, card.text.romaji) if word is not None]

    for word in words:
        pass


def _update_sounds(deck, cfg):
    """Update sound field of all cards in the deck."""

    downloads_dir = cfg.downloads_dir
    sounds_dir = cfg.sounds_dir
    sounds_ext = cfg.sounds_ext
    sounds_prefix = cfg.sounds_prefix

    for card in deck:
        if card.has_sound(sounds_dir):
            continue

        sound = _find_sound(card, downloads_dir, sounds_dir, sounds_ext, sounds_prefix)

        if sound:
            if not card.media.sound:
                logging.info("sound file '%s' found, updating sound field", sound)
                card.media.sound = sound
        else:
            if card.media.sound:
                logging.warning("no sound file found for '%s', clearing sound field", str(card))
                card.media.sound = None


def update(deck, cfg):
    """Tool 'update' command."""

    _update_pictos(deck, cfg)
    _update_sounds(deck, cfg)

    # save updated deck
    deck.save()
