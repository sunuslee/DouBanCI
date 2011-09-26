import urllib.request
import time
def get_shortenurl(long_url):
        data = '{"longUrl": ' + '"{0}"'.format(long_url) + "}"
        try:
                req = urllib.request.Request("https://www.googleapis.com/urlshortener/v1/url", data, {'Content-Type': 'application/json'})
                rec = urllib.request.urlopen(req).read()
                for s in rec.decode().split('"'):
                        if "http://goo.gl" in s:
                                return s
        except:
                f = open("url_log", "a+")
                f.write("{0}Short URL IS UNAVAILABLE NOW! long_url : {1}\n".format(time.ctime(), long_url))
                f.close()
                return None

def get_longurl(Short_url):
        try:
                req = urllib.request.urlopen('https://www.googleapis.com/urlshortener/v1/url?shortUrl={0}'.format(Short_url))
                rec = req.read()
                for s in rec.decode().split('"'):
                        if "http" in s and "goo.gl" not in s:
                                return s
        except:
                f = open("url_log", "a+")
                f.write("{0} LONG URL IS UNAVAILABLE NOW! Short_url : {1}\n".format(time.ctime(), Short_url))
                f.close()
                return None
