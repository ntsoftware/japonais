"""Tool 'check' command."""

import logging
import sys


def check(deck, cfg):
    """Tool 'check' command."""

    missing_pictos = 0
    missing_sounds = 0

    pictos_dir = cfg.pictos_dir
    sounds_dir = cfg.sounds_dir

    for card in deck:
        picto = card.media.picto
        if picto:
            if not card.has_picto(pictos_dir):
                logging.error("picto file '%s' does not exist", picto)
                missing_pictos += 1
            else:
                logging.debug("picto file '%s' exists", picto)

        sound = card.media.sound
        if sound:
            if not card.has_sound(sounds_dir):
                logging.error("sound file '%s' does not exist", sound)
                missing_sounds += 1
            else:
                logging.debug("sound file '%s' exists", sound)

    if missing_pictos:
        logging.error("%d pictos missing from pictos directory", missing_pictos)
    if missing_sounds:
        logging.error("%d sounds missing from sounds directory", missing_sounds)

    if missing_pictos or missing_sounds:
        sys.exit(1)
    else:
        sys.exit(0)
