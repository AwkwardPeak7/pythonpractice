#!/usr/bin/env python
import sys,json,requests
import xml.etree.cElementTree as e

try:
    manga_id = sys.argv[1]
except IndexError:
    print('No Manga ID Specified', file=sys.stderr)
    exit(1)

manga_info_url = "https://api.mangadex.org/manga/" + manga_id

manga_feed_url = "https://api.mangadex.org/manga/{}/feed".format(manga_id)
feed_parms= {'translatedLanguage[]':'en' , 'order[chapter]':'desc'}

manga_info = json.loads(requests.get(manga_info_url).content)
manga_feed = json.loads(requests.get(manga_feed_url,parms=feed_parms).content)

rss = e.Element("channel")
e.SubElement(rss,"title").text = manga_info['data']['attributes']['title']['en']
