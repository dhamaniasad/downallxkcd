import requests
import urllib
from bs4 import BeautifulSoup

nums = range(1, 1440)
urls = ["http://xkcd.com/" + str(num) for num in nums]
for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    soup2 = soup.find(id="comic")
    tag = soup2.img
    type(tag)
    imgurl = tag['src']
    imgname = soup.title.string
    imgfilename = "images/%s.jpg" % imgname
    getimg = urllib.urlretrieve(imgurl, imgfilename)
