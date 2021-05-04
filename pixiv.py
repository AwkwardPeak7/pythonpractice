#!/usr/bin/env python
import sys,json,re,requests,os

# regex which matches pixiv artwork urls and artwork id is the first capture block
pixiv_regex='^(?:https?:\/\/)?(?:www\.)?pixiv\.net\/(?:(?:\w\w\/)?artworks\/|member_illust\.php\?mode=(?:[^&]+&)+?illust_id=)(\d+).*'

# match url against regex
def match(regex,url):
    if re.compile(r'%s' % regex).match(url):
        pass
    else:
        # we catch this exception in the try block later
        raise Exception("invalid url")

# return capture block from url according to url
def search(regex,url):
    # the first capture block
    pic_id = re.search(r'%s' % regex, url).group(1)
    return pic_id

def main():
    try:
        # url passed as first command line argument
        pixiv_url=sys.argv[1]
        # url checked against the regex
        match(pixiv_regex,pixiv_url)
    # incase of no command line argument
    except IndexError:
        print('Error: no url provided', file=sys.stderr)
        exit(1)
    # incae of url not matching against regex
    # the exception raised in match() caught here
    except Exception as e:
        print('Error:', e, file=sys.stderr)
        exit(1)

    # the ajax url with artwork id at end
    artwork_id = search(pixiv_regex,pixiv_url)
    json_url = 'https://www.pixiv.net/ajax/illust/' + artwork_id

    # a get request to ajax url
    json_raw = requests.get(json_url).content
    # the server responce data parsed as json
    json_data = json.loads(json_raw)

    # look for .error in json
    if json_data['error'] == True:
        print("Error: no such image", file=sys.stderr)
        exit(1)

    # look for .body.pageCount in json
    max_num = json_data['body']['pageCount']
    # look for .body.urls.original in json
    url = json_data['body']['urls']['original']

    direct_urls = []
    cwd = os.getcwd() + '/'
    # number of urls is .body.pageCount or max_num
    for i in range(0,max_num):
        # create correct urls
        direct_urls.append(url.replace("_p0","_p"+str(i)))

        picture = requests.get(direct_urls[i], headers = {"Referer": "https://www.pixiv.net/"})
        open(cwd + os.path.basename(direct_urls[i]), 'wb').write(picture.content)

if __name__ == '__main__':
    main()
