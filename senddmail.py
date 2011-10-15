#!/usr/bin/env python3.1
# -*- coding: UTF-8 -*-

import random
import time
import urllib.parse
APIKEY = '053caab0d0224c680fb600127066e538'
SECRET = 'f2bebed97e85be8a'
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def get_rand_str(strlen):
        strlen = int(strlen)
        randstr = ''
        while strlen > 0:
                randstr += chars[random.randint(0, len(chars) - 1)]
                strlen -= 1
        return randstr
def make_args(method = None, url = None):
        args = {}
        args['oauth_consumer_key'] = APIKEY
        args['oauth_nonce'] = get_rand_str(16)
        args['oauth_signature_method'] = 'HMAC-SHA1'
        args['oauth_timestamp'] = int(time.time())
        s = ''
        for item in sorted(args.items(), key=lambda e:e[0]):
                s += '{0}={1}&'.format(str(item[0]), str(item[1]))
        s = s[0:-1] #delete last &
        print(s)
        url = urllib.parse.quote(url, safe = '')
        s = method + '&' +  url + s
make_args('GET', 'http://www.baidu.com')
