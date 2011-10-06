#!/usr/bin/env python3.1

import threading
import time
import fcntl
import urllib.request
import queue
import os

LOCK_EX = fcntl.LOCK_EX
LOCK_UN = fcntl.LOCK_UN
LOCK_NB = fcntl.LOCK_NB

APIKEY = "053caab0d0224c680fb600127066e538"
def download_t(url, filename):
        print('fuck this func', filename)
        while True:
                try:
                        fh = open("api_limit", "a+")
                        fcntl.flock(fh.fileno(), LOCK_EX|LOCK_NB)
                        break
                except IOError:
                        fh.close()
        print(filename, 'got the lock')
        if(fh.tell() != 0):
                os.lseek(fh.fileno(), -20, os.SEEK_END)
                line = fh.read(19)
                seconds = float(line.split()[1])
                while float(time.time()) - seconds <= 3.0:
                        pass
        fh.write("[LOG] {0:<24} {1} {2}\n".format(time.ctime(), url[:-40], time.time().__repr__()[0:-4]))
        fcntl.flock(fh, LOCK_UN)
        fh.close()
        print(filename, 'release the lock')
        data = urllib.request.urlopen(url).read().decode('utf8')
        print(filename, 'got the data')
        fw = open(filename, "w+")
        fw.write(data)
        fw.close()
        print('creat file:' ,filename)

def download_main(uid, cat, queue):
        start = 1
        url = "http://api.douban.com/people/{0}/collection?cat={1}&tag=&status=&start-index={2}&max-results=50&alt=atom&apykey={3}".format(uid, cat, start,APIKEY)
        while True:
                try:
                        fh = open("api_limit", "a+")
                        fcntl.flock(fh.fileno(), LOCK_EX|LOCK_NB)
                        break
                except IOError:
                        fh.close()
        if(fh.tell() != 0):
                os.lseek(fh.fileno(), -20, os.SEEK_END)
                line = fh.read(19)
                seconds = float(line.split()[1])
                while float(time.time()) - seconds <= 3.0:
                        pass
        data = urllib.request.urlopen(url).read().decode('utf8')
        fh.write("[LOG] {0:<24} {1} {2}\n".format(time.ctime(), url[:-40], time.time().__repr__()[0:-4]))
        fcntl.flock(fh, LOCK_UN)
        fh.close()
        filename = "{0}_{1}_{2}".format(uid, cat, start)
        fw = open(filename, "w+")
        fw.write(data)
        fw.close()
        fr = open(filename)
        for line in fr.readlines():
                if 'totalResults' in line:
                        max_item = int(line.split('>')[1].split('<')[0])
                        fr.close()
                        break
        dl_nr = max_item//50
        start += 50
        filename = "{0}_{1}_{2}".format(uid, cat, start)
        url = "http://api.douban.com/people/{0}/collection?cat={1}&tag=&status=&start-index={2}&max-results=50&alt=atom&apykey={3}".format(uid, cat, start,APIKEY)
        if max_item <= 50:
                return
        for i in range(dl_nr):
                url = "http://api.douban.com/people/{0}/collection?cat={1}&tag=&status=&start-index={2}&max-results=50&alt=atom&apykey={3}".format(uid, cat, start,APIKEY)
                filename = "{0}_{1}_{2}".format(uid, cat, start)
                queue.put([url, filename])
                start += 50
