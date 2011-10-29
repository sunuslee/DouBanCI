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
#import url3
#       Be careful to import url3 instead of url2
IS_LOCAL = False
ROOTDIR = "/home/sunus/apache/" if IS_LOCAL == True else "/usr/local/apache2/"
HOSTNAME = "http://10.10.149.18/"  if IS_LOCAL == True else "http://184.164.137.154/"

API_KEY = '053caab0d0224c680fb600127066e538'
SECRET = 'f2bebed97e85be8a'

cat_chs = {'movie':'电影','music':'音乐','book':'书籍'}
def main():
        global cat_chs
        print("Content-type:text/html; charset=UTF-8\r\n\r\n")
        print("<html>\n")
        print("<head>\n")
        print('<meta http-equiv="content-type" content="text/html; charset=utf8" />\n')
        print("<title>Verification</title>\n")
        print("</head>\n")
        print("<body>\n")
        form = cgi.FieldStorage()
        you = form.getvalue("you", None)
        exp_code = form.getvalue("exp_code", None)
        if argchk.exp_check(you, exp_code) == False:
                print("<h2>Sorry:(</h2>")
                print("<h2>This page is now only for testing users only</h2>")
                print("<h2>you:{0}<br>code:{1}".format(you, exp_code))
                print("</body>")
                print("</html>")
                return
        group_url = form.getvalue("group_url", "http://www.douban.com/group/maths/")
        if group_url.endswith('/') == False:
                group_url += '/'
        location = form.getvalue("location", None)
        location = location.decode('utf8')
        cat = form.getvalue("cat", None)
        anonymous = 0
        nickname = get_names.get_nickname(you)
        group_name = get_names.get_group_name(group_url)
        suffix = str(int(time.time()))
        longurl = HOSTNAME + "history/group_{0}_{1}_{2}.html".format(you, group_url.rsplit('/', 2)[1], suffix)
        short_url = url2.get_shortenurl(longurl)
        #short_url = short_url.encode()
        html_page_path = ROOTDIR + "htdocs/history/group_{0}_{1}_{2}.html".format(you, group_url.rsplit('/', 2)[1], suffix)
        entry = '\t'.join((you, nickname, group_url, group_name, location, cat, '0', short_url, html_page_path, suffix))
        # usr suffix as a oauth login verifier,too
        #entry = you + '\t' + nickname + '\t' + group_url + '\t' + group_name + '\t' + location + '\t' + cat + '\t' + '0' + 
        user_queue.add_user(entry)
        clientp = service.DoubanService(api_key=API_KEY, secret = SECRET)
        clientp.client.login(Parent = clientp, sid=suffix)
        print("</body>\n")
        print("</html>")

if __name__ == '__main__':
        main()
