import urllib.request
def get_shortenurl(long_url):
        data = '{"longUrl": ' + '"{0}"'.format(long_url) + "}"
        try:
                req = urllib.request.Request("https://www.googleapis.com/urlshortener/v1/url", data, {'Content-Type': 'application/json'})
                rec = urllib.request.urlopen(req).read()
                for s in rec.decode().split('"'):
                        if "http://goo.gl" in s:
                                return s
        except:
                print("<h4>Short URL IS UNAVAILABLE NOW!</h4>")
                pass

def get_longurl(Short_url):
        try:
                req = urllib.request.urlopen('https://www.googleapis.com/urlshortener/v1/url?shortUrl={0}'.format(Short_url))
                rec = req.read()
                for s in rec.decode().split('"'):
                        if "http" in s and "goo.gl" not in s:
                                return s
        except:
                print("<h4>Invaid URL CODE</h4>")
                pass
