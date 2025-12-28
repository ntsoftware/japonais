"""Card model."""

from dataclasses import dataclass


@dataclass
class CardText:
    """Card text."""
    fr: str
    ja: str
    furigana: str
    romaji: str


@dataclass
class CardMedia:
    """Card media."""
    picto: str
    sound: str


@dataclass
class Card:
    """Card model."""
    guid: int
    text: CardText
    media: CardMedia
    tags: [str]
