#!/usr/bin/env python3.1

import threading
import time
import fcntl
import urllib.request
import queue
import os
IS_LOCAL = True
LOCK_EX = fcntl.LOCK_EX
LOCK_UN = fcntl.LOCK_UN
LOCK_NB = fcntl.LOCK_NB

ROOTDIR = "/home/sunus/apache/" if IS_LOCAL == True else "/usr/local/apache2/"
APIKEY = "053caab0d0224c680fb600127066e538"
def download_t(uid, cat, start, queue, t_name):
        url = "http://api.douban.com/people/{0}/collection?cat={1}&tag=&status=&start-index={2}&max-results=50&alt=atom&apykey={3}".format(uid, cat, start,APIKEY)
        filename = '{0}_{1}_{2}'.format(uid, cat, start)
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
        fh.write("[LOG] {0:<24} {1} {2}\n".format(time.ctime(), url[:-40], time.time().__repr__()[0:-4]))
        fcntl.flock(fh, LOCK_UN)
        fh.close()
        print('start dl:{0} {1}'.format(t_name, time.ctime()))
        data = urllib.request.urlopen(url).read().decode('utf8')
        fw = open(ROOTDIR + r'htdocs/cache_datas/' + filename, "w+")
        fw.write(data)
        fw.close()
        print('creat file:' ,filename, time.ctime())
        if start == 1:
                fr = open(ROOTDIR + r'htdocs/cache_datas/' + filename)
                for line in fr.readlines():
                        if 'totalResults' in line:
                                max_item = int(line.split('>')[1].split('<')[0])
                                dl_nr = max_item//50
                                break
                if max_item > 50:
                        for i in range(dl_nr):
                                start += 50
                                queue.put([uid, cat, start, queue])
