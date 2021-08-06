#!/usr/bin/env python
"""
This script takes Mangadex manga uuid as first argument and creates
rss feed for the manga using the official Mangadex v5 api

The UUID can be found in the url of the manga information page e.g:
    url is https://mangadex.org/title/d86cf65b-5f6c-437d-a0af-19a31f94ec55
    uuid in this case is d86cf65b-5f6c-437d-a0af-19a31f94ec55
    uuid is basically the last part of random characters in the url
"""

import sys,json,requests
import xml.etree.cElementTree as ET
from io import BytesIO

try:
    manga_id = str(sys.argv[1])
except IndexError:
    print('No Manga ID Specified', file=sys.stderr)
    exit(1)

lang = 'en'

manga_info_url = "https://api.mangadex.org/manga/" + manga_id

manga_feed_url = "https://api.mangadex.org/manga/{}/feed".format(manga_id)
feed_parms= {'translatedLanguage[]':lang , 'order[chapter]':'desc' , 'limit':10}

manga_info = json.loads(requests.get(manga_info_url).content)

if manga_info["result"] == "error":
    print('Invalid Manga ID Specified', file=sys.stderr)
    exit(2)

manga_feed = json.loads(requests.get(manga_feed_url,params=feed_parms).content)

## rss building starts here

root = ET.Element("rss")
root.set("version","2.0")

channel = ET.SubElement(root,"channel")

ET.SubElement(channel,"title").text = manga_info['data']['attributes']['title'][lang]
ET.SubElement(channel,"link").text  = "https://mangadex.org/title/" + manga_id
ET.SubElement(channel,"description").text = manga_info['data']['attributes']['description'][lang]

items = []
count = 0

for result in manga_feed["results"]:
    items.append('') # increase size of array
    items[count] = ET.SubElement(channel,"item")
    ET.SubElement(items[count],"title").text = "Chapter " + result["data"]["attributes"]["chapter"]
    ET.SubElement(items[count],"description").text = result["data"]["attributes"]["title"]
    ET.SubElement(items[count],"link").text  = "https://mangadex.org/chapter/" + result["data"]["id"]
    ET.SubElement(items[count],"pubDate").text = result["data"]["attributes"]["publishAt"]
    count += 1

f = BytesIO()
rss_feed = ET.ElementTree(root)
rss_feed.write(f, encoding='utf-8', xml_declaration=True)
print(f.getvalue().decode('utf-8'))
