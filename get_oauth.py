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

API_KEY = '053caab0d0224c680fb600127066e538'
SECRET = 'f2bebed97e85be8a'
cat_chs = {'movie':'电影','music':'音乐','book':'书籍'}
def main():
        global cat_chs
        form = cgi.FieldStorage()
        you = form.getvalue("you", "sunus")
        group_url = form.getvalue("group_url", "http://www.douban.com/group/maths/")
        if group_url.endswith('/') == False:
                group_url += '/'
        location = form.getvalue("location", "天津")
        location = location.decode('utf8')
        cat = form.getvalue("cat", "movie")
        anonymous = 0
        nickname = get_names.get_nickname(you)
        group_name = get_names.get_group_name(group_url)
        entry = you + '\t' + nickname + '\t' + group_url + '\t' + group_name + '\t' + location + '\t' + cat + '\t' + '0'
        user_queue.add_user(entry)
        print("Content-type:text/html; charset=UTF-8\r\n\r\n")
        print("<html>\n")
        print("<head>\n")
        print('<meta http-equiv="content-type" content="text/html; charset=utf8" />\n')
        print("<title>Verification</title>\n")
        print("</head>\n")
        print("<body>\n")
        clientp = service.DoubanService(api_key=API_KEY, secret = SECRET)
        clientp.client.login(Parent = clientp)
        print("</body>\n")
        print("</html>")

if __name__ == '__main__':
        main()
