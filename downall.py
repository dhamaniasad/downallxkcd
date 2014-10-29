import requests
import urllib
from bs4 import BeautifulSoup
import re

nums = range(1, 1440)
urls = ["http://xkcd.com/" + str(num) for num in nums]
for url in urls:
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        soup2 = soup.find(id="comic")
        tag = soup2.img
        type(tag)
        imgurl = tag['src']
        imgname = soup.title.string
        imgname = re.sub(r'[^a-zA-Z0-9 ]', '', imgname)
        imgname = re.sub('xkcd ', '', imgname)
        if imgurl.endswith(('.jpg')):
            imgfilename = "images/%s.jpg" % imgname
        else:
            imgfilename = "images/%s.png" % imgname
        getimg = urllib.urlretrieve(imgurl, imgfilename)
    except Exception:
        print "Failed for", url
