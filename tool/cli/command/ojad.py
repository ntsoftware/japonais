"""Tool 'ojad' command."""

from tool.service.ojad import get_accents


def ojad(args):
    """Tool 'ojad' command."""

    for word in args.words:
        accents = get_accents(word)

        for html in accents.values():
            print(html)
