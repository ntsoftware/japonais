"""Forvo web service."""

import logging
import re
import requests


def download_pronunciations(word, cookie, output_dir):
    """Download pronunciations for a word."""

    url = f"https://fr.forvo.com/word/{word}"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Alt-Used": "fr.forvo.com",
        "Cookie": cookie,
    }

    logging.info("get pronunciation info for word '%s'", word)
    r = requests.get(url, headers=headers, timeout=5)

    if r.status_code != 200:
        logging.error("get request failed (%d)", r.status_code)
        return None

    urls = []

    for line in r.text.splitlines():
        if "Télécharger en MP3" in line:
            m = re.search('data-p1="(.*)" data-p2="(.*)" data-p3="(.*)" data-p4="(.*)"', line)

            p2 = m.group(2)
            p3 = m.group(3)
            p4 = m.group(4)

            if p3 == "ja":
                url = f"https://fr.forvo.com/download/mp3/{p2}/{p3}/{p4}"
                urls.append(url)

    logging.info("found %d pronunciations for word '%s'", len(urls), word)

    files = []

    for i, url in enumerate(urls):
        r = requests.get(url, headers=headers, timeout=5)

        if r.status_code != 200:
            logging.error("get request failed (%d)", r.status_code)
            continue

        content_type = r.headers["Content-Type"].partition(";")[0]
        content = r.content

        if content_type != "application/octet-stream":
            logging.error("content type is not binary (%s)", content_type)
            continue

        output_file = output_dir.joinpath(f"pronunciation_ja_{word}({i+1}).mp3")
        output_file.parent.mkdir(exist_ok=True, parents=True)

        logging.info("write pronunciation file '%s' (%d bytes)", output_file, len(content))
        with open(output_file, "wb") as f:
            f.write(content)

        files.append(output_file)

    return files
