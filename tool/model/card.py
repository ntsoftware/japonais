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

    def __str__(self):
        """TODO"""

    def has_picto(self, pictos_dir):
        """Check if the card has a picto and the picto file exists."""

        picto = self.media.picto
        if picto:
            picto_file = pictos_dir.joinpath(picto)
            if picto_file.is_file():
                return True

        return False

    def has_sound(self, sounds_dir):
        """Check if the card has a sound and the sound file exists."""

        sound = self.media.sound
        if sound:
            sound_file = sounds_dir.joinpath(sound)
            if sound_file.is_file():
                return True

        return False
