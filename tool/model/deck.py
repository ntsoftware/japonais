"""Deck model."""

import logging
import re

from csv import DictReader, DictWriter
from dataclasses import dataclass
from io import StringIO
from pathlib import Path

from .card import Card, CardMedia, CardText


def _parse_picto(field, ext):
    """Parse a CSV picto field."""
    if field:
        m = re.match(r'<img src="(.*)">', field)
        if m:
            picto = m.group(1).strip()
            if not picto.endswith(ext):
                logging.warning("picto file '%s' extension is not '%s'", picto, ext)
            else:
                return picto
        else:
            logging.error("invalid picto field '%s'", field)


def _format_picto(picto):
    """Format a CSV picto field."""
    return f'<img src="{picto}">' if picto else ""


def _parse_sound(field, ext, prefix):
    """Parse a CSV sound field."""
    if field:
        m = re.match(r'\[sound:(.*)\]', field)
        if m:
            sound = m.group(1).strip()
            if not sound.endswith(ext):
                logging.warning("sound file '%s' extension is not '%s'", sound, ext)
            elif not sound.startswith(prefix):
                logging.warning("sound file '%s' prefix is not '%s'", sound, prefix)
            else:
                return sound
        else:
            logging.error("invalid sound field '%s'", field)


def _format_sound(sound):
    """Format a CSV sound field."""
    return f'[sound:{sound}]' if sound else ""


def _parse_tags(field):
    """Parse a CSV tagsfield."""
    if field:
        return field.split()


def _format_tags(tags):
    """Format a CSV tags field."""
    return " ".join(tags) if tags else ""


@dataclass
class DeckConfig:
    """Deck configuration."""
    filename: Path
    fieldnames: [str]
    headers: [str]
    delimiter: str


class Deck:
    """Deck model."""

    def __init__(self, cards, cfg):
        self._cards = cards
        self._cfg = cfg

    def __len__(self):
        return len(self._cards)

    def __iter__(self):
        return iter(self._cards)

    def save(self):
        """Save the deck to a CSV file."""
        with open(self._cfg.filename, "w", encoding="utf-8", newline="") as f:
            for header in self._cfg.headers:
                f.write(header)

            writer = DictWriter(f, fieldnames=self._cfg.fieldnames, delimiter=self._cfg.delimiter, lineterminator="\n")

            for card in self._cards:
                row = {
                    "id": card.guid,
                    "fr": card.text.fr,
                    "ja": card.text.ja,
                    "furigana": card.text.furigana,
                    "romaji": card.text.romaji,
                    "picto": _format_picto(card.media.picto),
                    "sound": _format_sound(card.media.sound),
                    "tags": _format_tags(card.tags),
                }

                writer.writerow(row)


class InvalidSeparatorError(Exception):
    """Invalid separator."""
    def __init__(self, sep):
        self.sep = sep
        super().__init__(f"invalid separator '{sep}'")


def load(cfg):
    """Load a deck from a CSV file."""
    deck_file = cfg.deck_file

    with open(deck_file, "r", encoding="utf-8", newline="") as f:
        lines = f.readlines()

    headers = []
    delimiter = "\t"
    fieldnames = cfg.deck_columns

    while lines and lines[0].startswith("#"):
        line, *lines = lines
        headers.append(line)

        if line.startswith("#separator:"):
            sep = line.removeprefix("#separator:").strip().lower()
            if sep == "comma":
                delimiter = ","
            elif sep == "semicolon":
                delimiter = ";"
            elif sep == "tab":
                delimiter = "\t"
            elif sep == "space":
                delimiter = " "
            elif sep == "pipe":
                delimiter = "|"
            elif sep == "colon":
                delimiter = ":"
            else:
                raise InvalidSeparatorError(sep)

        if line.startswith("#columns:"):
            fieldnames = line.removeprefix("#columns:").strip("\n").split(delimiter)

    reader = DictReader(StringIO("".join(lines)), fieldnames=fieldnames, delimiter=delimiter)

    cards = []

    pictos_ext = cfg.pictos_ext
    sounds_ext = cfg.sounds_ext
    sounds_prefix = cfg.sounds_prefix

    for row in reader:
        card_text = CardText(
            fr=row["fr"],
            ja=row["ja"],
            furigana=row["furigana"],
            romaji=row["romaji"],
        )

        card_media  = CardMedia(
            picto=_parse_picto(row["picto"], pictos_ext),
            sound=_parse_sound(row["sound"], sounds_ext, sounds_prefix),
        )

        cards.append(Card(
            guid=int(row["id"]),
            text=card_text,
            media=card_media,
            tags=_parse_tags(row["tags"]),
        ))

    deck_cfg = DeckConfig(
        filename=deck_file,
        fieldnames=fieldnames,
        headers=headers,
        delimiter=delimiter,
    )

    return Deck(cards, deck_cfg)
