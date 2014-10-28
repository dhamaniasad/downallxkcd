import requests

for x in xrange(1440):
    r = requests.get("http://xkcd.com/%s" % x)
    html = r.content
    print html