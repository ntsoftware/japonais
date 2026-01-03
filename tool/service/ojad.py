"""OJAD web service."""

import logging
import lxml.html
import requests


def _get_furigana(chars):
    """Get furigana pronunciation."""

    return "".join([c for c, _ in chars])


def _get_html(chars):
    """Get HTML fragement of the pronunciation."""

    elements = []
    accent = 0

    for c, char_accent in chars:

        if char_accent != accent:
            if accent == 2:
                elements.append("</b>")
            elif accent == 1:
                elements.append("</u>")

            if char_accent == 2:
                elements.append("<b>")
            elif char_accent == 1:
                elements.append("<u>")

            accent = char_accent

        elements.append(c)

    if accent == 2:
        elements.append("</b>")
    elif accent == 1:
        elements.append("</u>")

    return "".join(elements)


def get_accents(word):
    """Get accent for a word as HTML fragment."""

    url = f"https://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/word:{word}"

    logging.info("get accents for word '%s'", word)
    r = requests.get(url, timeout=5)

    if r.status_code != 200:
        logging.error("get request failed (%d)", r.status_code)
        return None

    text = r.text
    html = lxml.html.fromstring(text)

    words = html.cssselect(".katsuyo.katsuyo_jisho_js .accented_word")

    if not words:
        logging.error("no accents found for word '%s'", word)
        return None

    accents = {}

    for w in words:
        spans = w.cssselect(".accented_word > span")
        chars = []

        for span in spans:
            s = span.text_content()

            if 'accent_top' in span.classes:
                chars.append((s, 2))
            elif 'accent_plain' in span.classes:
                chars.append((s, 1))
            else:
                chars.append((s, 0))

        furigana = _get_furigana(chars)
        html = _get_html(chars)

        accents[furigana] = html

    return accents
