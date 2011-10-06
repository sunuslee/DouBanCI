#!/usr/bin/env python3.1

import os
import random
import time
import multiprocessing
import urllib.request
import urllib.parse
import fcntl
LOCK_EX = fcntl.LOCK_EX
LOCK_UN = fcntl.LOCK_UN
LOCK_NB = fcntl.LOCK_NB
que = multiprocessing.JoinableQueue()
people_list = []
people_nr = 35
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
        pid = os.fork()
        print('pid =' , pid)
        if pid == 0:
                APIKEY = "053caab0d0224c680fb600127066e538"
                while True:
                        while True:
                                try:
                                        fh = open('time', 'r+')
                                        fcntl.flock(fh, LOCK_EX|LOCK_NB)
                                        break
                                except IOError:
                                        fh.close()
                        os.lseek(fh.fileno(), 0, os.SEEK_SET)
                        lt = float(fh.read())
                        while time.time() - lt < 2.5:
                                continue
                        if que.empty() == False:
                                uid, cat, start = que.get()
                                if uid == None:
                                        os.lseek(fh.fileno(), 0, os.SEEK_SET)
                                        fh.write(repr(time.time()))
                                        fh.flush()
                                        fcntl.flock(fh, LOCK_UN)
                                        fh.close()
                                        print('uid = None')
                                        que.task_done()
                                        break
                                print('get {0:<16} cat:{1:<10} start{2:<3}'.format(uid, cat, start))
                                url = "http://api.douban.com/people/{0}/collection?cat={1}&tag=&status=&start-index={2}&max-results=50&alt=atom&apykey={3}".format(uid, cat, start,APIKEY)
                                filename = '{0}_{1}_{2}'.format(uid, cat, start)
                                data = urllib.request.urlopen(url).read().decode('utf8')
                                print('\t\t\t\t\tapi date:{0}'.format(time.ctime()))
                                fw = open(filename, 'w')
                                fw.write(data)
                                fw.close()
                                print('\t\t\t\t\tcreat file {0}'.format(filename))
                                que.task_done()
                                os.lseek(fh.fileno(), 0, os.SEEK_SET)
                                fh.write(repr(time.time()))
                                fh.flush()
                                fcntl.flock(fh, LOCK_UN)
                                fh.close()
        else:
                while True:
                        cat = 'movie'
                        for i in range(35):
                                start = 1
                                print('put {0} start 1'.format(people_list[i][0]))
                                que.put([people_list[i][0], cat, start])
                                filename = '{0}_{1}_{2}'.format(people_list[i][0], cat, start)
                                while True:
                                        try:
                                                fr = open(filename)
                                                for line in fr.readlines():
                                                        if 'totalResults' in line:
                                                                max_item = int(line.split('>')[1].split('<')[0])
                                                                fr.close()
                                                                url_put = max_item//50
                                                                for idx in range(url_put):
                                                                        start += 50
                                                                        que.put([people_list[i][0], cat, start])
                                                                        print('{0:<16} max:{1:<3} put idx{2:<3}'.format(people_list[i][0], max_item, start))
                                                                break
                                                break
                                        except IOError:
                                                pass
                        que.put([None, None, None])
                        break

        if pid == 0:
                print('[child] ends')
        else:
                print('[Parent] ends')
                que.join()

if __name__ == '__main__':
        main()
