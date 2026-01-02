"""Tool 'ojad' command."""

from tool.service.ojad import get_accent


def ojad(args):
    """Tool 'ojad' command."""

    for word in args.words:
        accent = get_accent(word)
        print(accent)
