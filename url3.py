#!/usr/bin/python2.6

import random
import pickle

# ONLY USE THIS MODULE WHEN YOU HAVE A *REAL DOMAIN*
IS_LOCAL = True
PAGEDIR  = '/home/sunus/apache/htdocs/' if IS_LOCAL == True else '/usr/local/apache2/htdocs/'
HOSTNAME = 'http://10.10.149.18/'  if IS_LOCAL == True else 'http://184.164.137.154/'
RETFILE  = 'http://10.10.149.18/r/showresult.py?'
charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def get_randstr(length):
        randstr = []
        while length:
                randstr.append(charset[random.randint(0,61)])
                length -= 1
        randstr = ''.join(randstr)
        return randstr

#page_path is the absolute path.
def get_shortenurl(long_url):
        #path = PAGEDIR + '/'.join(long_url.split('/')[3:])
        try:
                f_url_dict = open('./URL_DICT', 'rb')
                url_dict = pickle.load(f_url_dict)
        except IOError:
                url_dict = {}
        while True:
                redirect_code = get_randstr(4)
                if redirect_code not in url_dict:
                        url_dict[redirect_code] = long_url
                        f_url_dict = open('./URL_DICT', 'wb')
                        pickle.dump(url_dict, f_url_dict)
                        f_url_dict.close()
                        return RETFILE + redirect_code

def get_longurl(Short_url):
        try:
                redirect_code = Short_url[-4:]
                f_url_dict = open('./URL_DICT', 'rb')
                url_dict = pickle.load(f_url_dict)
                f_url_dict.close()
                long_url = url_dict[redirect_code]
                return long_url
        except (IOError, LookupError):
                print('Wrong Short Url')


def test():
        su = get_shortenurl('http://localhost/history/couple_3215295_sunus.html')
        print(su)
        lu = get_longurl(su)
        print(lu)
        su2 = get_shortenurl('http://localhost/history/group_kingsamchen_maths_82794591.html')
        print(su2)
        lu2 = get_longurl(su2)
        print(lu2)
