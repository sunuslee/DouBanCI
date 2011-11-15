#!/usr/bin/env python2.6
# -*- coding: UTF-8 -*-

import sys
import codecs
import atom
import gdata
import client
import service
import cgi
import get_names
import user_queue
import url2
import time
import argchk
import random
#import url3
#       Be careful to import url3 instead of url2
IS_LOCAL = True
ROOTDIR = "/home/sunus/apache/" if IS_LOCAL == True else "/usr/local/apache2/"
HOSTNAME = "http://10.10.149.18/"  if IS_LOCAL == True else "http://184.164.137.154/"

API_KEY = '053caab0d0224c680fb600127066e538'
SECRET = 'f2bebed97e85be8a'

cat_chs = {'movie':'电影','music':'音乐','book':'书籍'}
test_user = (   'sunus',
                'vivianlmw',
                'kingsamchen',
                'abysspheles',
                'aka',
                'feiye',
                'yemaomomo',
                'HDJ',
                'linda1204',
                '3215295',
                '3943880')
test_group = (  'http://www.douban.com/group/zhuangb/',
                'http://www.douban.com/group/tjpu/',
                'http://www.douban.com/group/kaopulove/',
                'http://www.douban.com/group/python/',
                'http://www.douban.com/group/geek_wife/',
                'http://www.douban.com/group/ai_Junko/',
                'http://www.douban.com/group/nasha/',
                'http://www.douban.com/group/Yi-club/',
                'http://www.douban.com/group/yahooks/',
                'http://www.douban.com/group/BigBangTheory/',
                'http://www.douban.com/group/thebigbang/',
                'http://www.douban.com/group/tjpu/')
test_location = ('天津','北京','南京','桂林','柳州','广州','武汉','石家庄', '南宁')
test_cat = ('movie', 'music', 'book')

def add_randuser():
        you = test_user[random.randint(0, 9)]
        group_url = test_group[random.randint(0, 10)]
        location = test_location[random.randint(0, 8)]
        cat = test_cat[random.randint(0, 2)]
        anonymous = 0
        if group_url.endswith('/') == False:
                group_url += '/'
        location = location.decode('utf8')
        nickname = get_names.get_nickname(you)
        group_name = get_names.get_group_name(group_url)
        suffix = str(int(time.time()))
        longurl = HOSTNAME + "history/group_{0}_{1}_{2}.html".format(you, group_url.rsplit('/', 2)[1], suffix)
        short_url = url2.get_shortenurl(longurl)
        html_page_path = ROOTDIR + "htdocs/history/group_{0}_{1}_{2}.html".format(you, group_url.rsplit('/', 2)[1], suffix)
        entry = '\t'.join((you, nickname, group_url, group_name, location, cat, '0', short_url, html_page_path))
        user_queue.add_user(entry)

def main():
        for i in range(13):
                add_randuser()
        return

if __name__ == '__main__':
        main()
