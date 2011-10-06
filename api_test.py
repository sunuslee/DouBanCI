#!/usr/bin/env python3.1
# -*- coding: UTF-8 -*-

import random
import urllib.request
import urllib.parse
import time
import datetime
APIKEY = "053caab0d0224c680fb600127066e538"
people_nr = 35
people_list = []
def get_user(group_uri, where):
        where = urllib.parse.quote(where)
        global people_list
        start = 13577293
        error = 0
        uri = "{0}/member_search?search_text={1}&start={2}".format(group_uri, where, start)
        fh = urllib.request.urlopen(uri)
        data = fh.read().decode("utf8")
        max = 0
        for line in data.splitlines():
                if str(13577294) in line:       # this num will SOMEHOW INCREASE 1
                        max = int(line.split('-')[1].split()[0])
        start = 0 if max == 0 else random.randint(0, int(max) - 35)
        print("<h4>你的幸运数字是 *{0}*</h4>".format(start))
        uri = "{0}/member_search?search_text={1}&start={2}".format(group_uri, where, start)
        fh = urllib.request.urlopen(uri)
        contents = fh.read().decode("utf8")
        for line in contents.splitlines():
                if '<dd><a href="http://www.douban.com/people/' in line:
                        if(len(people_list) == people_nr):
                                break
                        idx = line.strip().find(r'</a>')
                        a = line.strip()[0:idx].rpartition(r'">')
                        people_list.append([a[0][13:-1], a[2]])
        i = 0
        for i in range(len(people_list)):
                people_list[i][0] = people_list[i][0].rpartition("/")[2]

def main():
        group_url = "http://www.douban.com/group/python/"
        location = "天津"
        GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
        get_user(group_url, location)
        header = {'If-Modified-Since': 'Wed, 28 Sep 2011 09:50:50 GMT'}
        for i in range(900):
                try:
                        p = urllib.request.urlopen("http://api.douban.com/people/{0}?alt=atom&apikey={1}".format(people_list[i%35][0],APIKEY))
                        rec = p.read().decode("utf8")
                        print("cnt = {0} user = {1}\n".format(i, people_list[i%35][0]))
                        time.sleep(2.1)
                except (urllib.error.URLError, ValueError) as e:
                        if hasattr(e, 'reason'):
                                print("<h4>Cannot connected to the server</h4>")
                        if hasattr(e, 'code'):
                                print("<h4>Return code:",e.code,"error</h4>")
                                print("<h4>This username/group may not exsit</h4>")

        print("done")

if __name__ == "__main__":
        main()
