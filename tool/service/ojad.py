"""OJAD web service."""

import logging
import lxml.html
import requests


def get_accent(word):
    """Get accent for a word as HTML fragment."""

    url = f"https://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/word:{word}"

    logging.info("get accent for word '%s'", word)
    r = requests.get(url, timeout=5)

    if r.status_code != 200:
        logging.error("get request failed (%d)", r.status_code)
        return None

    text = r.text
    html = lxml.html.fromstring(text)

    words = html.cssselect(".katsuyo.katsuyo_jisho_js .accented_word")

    if not words:
        logging.error("no accent found for word '%s'", word)
        return None

    if len(words) != 1:
        logging.error("too many accents found for word '%s' (%d accents)", word, len(words))
        return None

    spans = words[0].cssselect(".accented_word > span")
    chars = []

    for span in spans:
        s = span.text_content()

        if 'accent_top' in span.classes:
            chars.append(f"<b>{s}</b>")
        elif 'accent_plain' in span.classes:
            chars.append(f"<u>{s}</u>")
        else:
            chars.append(s)

    return "".join(chars)
