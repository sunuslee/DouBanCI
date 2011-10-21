import urllib.request

class fake_broswer(urllib.request.Request):
        def __init__(self, url):
                self.fake_broswer_headers = {
                                'User-agent': 'Mozilla/5.0 (X11; Linux i686; rv:7.0.1) Gecko/20100101 Firefox/7.0.1', 
                                'Accept-encoding': 'identity', 
                                'Connection': 'keep-alive'}
                self.url = url
                self.request = urllib.request.Request(url, headers = {})

        def fbopen(self):
                return urllib.request.urlopen(self.request)

def test():
        fb = fake_broswer('http://www.douban.com/group/fangzi/')
        fb = fb.fbopen()
        cont = fb.read()
        cont = cont.decode('utf8')
        print(cont)

test()
