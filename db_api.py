import fcntl
import os
import urllib.request
import time
LOCK_EX = fcntl.LOCK_EX
LOCK_UN = fcntl.LOCK_UN
LOCK_NB = fcntl.LOCK_NB
LIMIT = 38
def try_api(api_url):
        while True:
                while True:
                        try:
                                fh = open("api_limit", "a+")
                                fcntl.flock(fh.fileno(), LOCK_EX|LOCK_NB)
                                break
                        except IOError:
                                fh.close()
                                time.sleep(1)

                if(fh.tell() == 0):
                        data = urllib.request.urlopen(api_url)
                        fh.write("[LOG] START at {0}\n".format(time.ctime()))
                        fh.write("[LOG] cnt == {0:2} {1:<24} {2}\n".format(1, time.ctime(), api_url[:-40]))
                        fh.write("{0},{1},{2}\n".format(time.ctime(), 1, int(time.time())))
                        break;
                os.lseek(fh.fileno(), -17, os.SEEK_END)
                lastline = fh.read(16)
                lasttime, cnt  = lastline.split(',')[-1:-3:-1] # get the last two element, cnt and lasttime 
                if(int(time.time()) - int(lasttime) >= 65):
                        cnt = 1
                        data = urllib.request.urlopen(api_url)
                        fh.write("[LOG] START at {0}\n".format(time.ctime()))
                        fh.write("[LOG] cnt == {0:2} {1:<24} {2}\n".format(1, time.ctime(), api_url[:-40]))
                        fh.write("{0},{1},{2}\n".format(time.ctime(), cnt, int(time.time())))
                        break
                elif int(cnt) >= LIMIT:
                        fh.write("[LOG] No More API at this time {0}\n".format(time.ctime()))
                        fh.write("[LOG] END at {0},0,{1}\n".format(time.ctime(), int(time.time())))
                        #fcntl.flock(fh.fileno(), LOCK_UN) JUST LET THE FILE KEEP ON BLOCKING WHILE IT'S SLEEPING , 25, 9, 2011
                        #I am not sure whether it will work or not:<
                        fh.close()
                        time.sleep(65)
                        #time.sleep(int(lasttime) + 65 - int(time.time()))
                else:
                        cnt = int(cnt)
                        cnt += 1
                        fh.write("[LOG] cnt == {0:2} {1:<24} {2}\n".format(cnt, time.ctime(), api_url[:-40]))
                        fh.write("{0},{1},{2}\n".format(time.ctime(), cnt, lasttime))
                        data = urllib.request.urlopen(api_url)
                        break

        fcntl.flock(fh.fileno(), LOCK_UN)
        fh.close()
        return data 
