#!/usr/bin/env python2.6
# -*- coding: UTF-8 -*-

import urllib2
import time
def get_shortenurl(long_url):
        data = '{"longUrl": ' + '"{0}"'.format(long_url) + "}"
        try:
                req = urllib2.Request("https://www.googleapis.com/urlshortener/v1/url", data, {'Content-Type': 'application/json'})
                rec = urllib2.urlopen(req).read()
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
                req = urllib2.urlopen('https://www.googleapis.com/urlshortener/v1/url?shortUrl={0}'.format(Short_url))
                rec = req.read()
                for s in rec.decode().split('"'):
                        if "http" in s and "goo.gl" not in s:
                                return s
        except:
                f = open("url_log", "a+")
                f.write("{0} LONG URL IS UNAVAILABLE NOW! Short_url : {1}\n".format(time.ctime(), Short_url))
                f.close()
                return None

def url_test():
        url = 'http://www.douban.com'
        print 'url test:\n'
        print url
        su = get_shortenurl(url)
        print su
        lu = get_longurl(su)
        print lu
        print 'test finished'


if __name__ == '__main__':
        url_test()
