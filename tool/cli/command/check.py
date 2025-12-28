"""Tool 'check' command."""

import logging


def check(deck, cfg):
    """Tool 'check' command."""
    for card in deck:
        picto = card.media.picto
        if picto:
            picto_file = cfg.pictos_dir.joinpath(picto)
            if not picto_file.is_file():
                logging.error("picto file '%s' does not exist", picto)

        sound = card.media.sound
        if sound:
            sound_file = cfg.sounds_dir.joinpath(sound)
            if not sound_file.is_file():
                logging.error("sound file '%s' does not exist", sound)
