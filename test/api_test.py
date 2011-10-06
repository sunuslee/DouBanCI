#!/usr/bin/env python3.1
# -*- coding: UTF-8 -*-

import random
import urllib.request
import urllib.parse
import time
import datetime
import threading
import queue
import dl
APIKEY = "053caab0d0224c680fb600127066e538"
people_nr = 35
people_list = []

class Worker(threading.Thread):

        def __init__(self, work_queue):
                super().__init__()
                self.work_queue = work_queue
        def run(self):
                while True:
                        try:
                                uid, cat, start, que  = self.work_queue.get()
                                tname = self.getName()
                                self.process(uid, cat, start, que, tname)
                        finally:
                                self.work_queue.task_done()
        
        def process(self, uid, cat, start, que, tname):
                dl.download_t(uid, cat, start, que, tname)

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
        get_user(group_url, location)
        # THREAD PART
        dl_queue = queue.Queue()
        for i in range(10):
                worker = Worker(dl_queue)
                worker.daemon = True
                worker.start()
        for i in range(35):
                dl_queue.put([people_list[i][0], 'movie', 1, dl_queue])
                print('[MAIN]put {0:32} idx{1:<5} {2:<2}left'.format(people_list[i][0], 1, 34 - i))
                dl_queue.join()
        # THREAD PART
        print("done")

if __name__ == "__main__":
        main()
