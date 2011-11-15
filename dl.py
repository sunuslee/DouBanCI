#!/usr/bin/env python3.1

import threading
import time
import fcntl
import urllib.request
import urllib.error
import queue
import os
import gzip
import io
LOCK_EX = fcntl.LOCK_EX
LOCK_UN = fcntl.LOCK_UN
LOCK_NB = fcntl.LOCK_NB

IS_LOCAL = True
ROOTDIR = "/home/sunus/apache/" if IS_LOCAL == True else "/usr/local/apache2/"
APIKEY = "053caab0d0224c680fb600127066e538"
EXIT = False
def download_t(uid, cat, start, queue, t_name):
        global EXIT
        url = "http://api.douban.com/people/{0}/collection?cat={1}&tag=&status=&start-index={2}&max-results=50&alt=atom&apikey={3}".format(uid, cat, start,APIKEY)
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
        # just be careful! 
        while float(time.time()) - seconds <= 1.8:
                pass
        fh.write("[LOG] {0:<24} {1} {2}\n".format(time.ctime(), url[:-40], time.time().__repr__()[0:-4]))
        fcntl.flock(fh, LOCK_UN)
        fh.close()
        #print('start dl:{0} {1}'.format(t_name, time.ctime()))
        try:
                req = urllib.request.Request(url, headers= {'Accept-encoding':'gzip'})
                rec = urllib.request.urlopen(req)
                compressed_data = rec.read()
                compressed_fh = io.BytesIO(compressed_data)
                gzipper = gzip.GzipFile(fileobj = compressed_fh);
                data = gzipper.read().decode('utf8')
                #data = urllib.request.urlopen(url).read().decode('utf8')
        except (urllib.error.URLError, ValueError) as e:
                if hasattr(e, 'reason'):
                        print("<h4>Cannot connected to the server</h4>")
                        print("<h4>url:</h4>",url)
                        EXIT = True
                        return
                if hasattr(e, 'code'):
                        print("<h4>Return code:",e.code,"error</h4>")
                        print("<h4>",e.msg,"</h4>")
                        print("<h4>url:</h4>",url)
                        EXIT = True
                        return
        fw = open(ROOTDIR + r'htdocs/cache_datas/' + filename, "w+", encoding = 'utf8')
        fw.write(data)
        fw.close()
        #print('creat file:' ,filename, time.ctime())
        if start == 1:
                fr = open(ROOTDIR + r'htdocs/cache_datas/' + filename, 'r', encoding = 'utf8')
                for line in fr.readlines():
                        if 'totalResults' in line:
                                max_item = int(line.split('>')[1].split('<')[0])
                                dl_nr = max_item//50
                                break
                if max_item > 50:
                        for i in range(dl_nr):
                                start += 50
                                queue.put([uid, cat, start, queue])

