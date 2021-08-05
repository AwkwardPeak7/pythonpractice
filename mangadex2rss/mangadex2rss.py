#!/usr/bin/env python
import sys,json,requests
import xml.etree.cElementTree as e

try:
    manga_id = sys.argv[1]
except IndexError:
    print('No Manga ID Specified', file=sys.stderr)
    exit(1)

try:
    lang = sys.argv[2]
except IndexError:
    lang = "en"

manga_info_url = "https://api.mangadex.org/manga/" + manga_id

manga_feed_url = "https://api.mangadex.org/manga/{}/feed".format(manga_id)
feed_parms= {'translatedLanguage[]':lang , 'order[chapter]':'desc'}
