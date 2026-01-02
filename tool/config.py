"""Tool configuration."""

from configparser import ConfigParser
from pathlib import Path


class Config:
    """Tool configuration."""

    def __init__(self, cfg):
        self._cfg = cfg

        with open(cfg.get("forvo", "cookie"), "r", encoding="utf-8") as f:
            self._forvo_cookie = f.read().strip()

    @property
    def anki_path(self):
        """Anki path."""
        return Path(self._cfg.get("anki", "path")).expanduser()

    @property
    def anki_user(self):
        """Anki user."""
        return self._cfg.get("anki", "user")

    @property
    def deck_file(self):
        """Deck file."""
        return Path(self._cfg.get("deck", "file")).expanduser()

    @property
    def deck_columns(self):
        """Deck columns."""
        return self._cfg.get("deck", "columns").split()

    @property
    def pictos_dir(self):
        """Pictos directory."""
        return Path(self._cfg.get("pictos", "path")).expanduser()

    @property
    def pictos_ext(self):
        """Pictos file extension."""
        return self._cfg.get("pictos", "ext", fallback=".png")

    @property
    def sounds_dir(self):
        """Sounds directory."""
        return Path(self._cfg.get("sounds", "path")).expanduser()

    @property
    def sounds_ext(self):
        """Sounds file extension."""
        return self._cfg.get("sounds", "ext", fallback=".mp3")

    @property
    def downloads_dir(self):
        """Downloads directory."""
        return Path(self._cfg.get("downloads", "path")).expanduser()

    @property
    def forvo_cookie(self):
        """Forvo session cookie."""
        return self._forvo_cookie


def load(path = "tool.ini"):
    """Load tool configuration."""
    cfg = ConfigParser()
    cfg.read(path)
    return Config(cfg)
