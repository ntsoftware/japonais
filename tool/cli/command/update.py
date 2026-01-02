"""Tool 'update' command."""

from tool import config, model
from tool.service.forvo import download_pronunciations
from tool.service.ojad import get_accent


def _update_accents(deck):
    """Update 'accent' fields."""

    for card in deck:
        if card.text.ja and not card.text.accent:
            accent = get_accent(card.text.ja)
            if accent:
                card.text.accent = accent


def _update_sounds(deck, cfg):
    """Update 'sound' fields."""

    for card in deck:
        if card.text.ja and not card.has_sound(cfg.sounds_dir):
            sounds = download_pronunciations(card.text.ja, cfg.forvo_cookie, cfg.sounds_dir)
            if sounds:
                card.media.sound = sounds[0].name


def _update_pictos(_deck, _cfg):
    """Update 'picto' fields."""


def update(_args):
    """Tool 'update' command."""

    cfg = config.load()

    deck = model.deck.load(cfg)

    _update_accents(deck)
    _update_sounds(deck, cfg)
    _update_pictos(deck, cfg)

    # save updated deck
    deck.save()
