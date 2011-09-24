import fcntl
import os
import urllib.request
import time
LOCK_EX = fcntl.LOCK_EX
LOCK_UN = fcntl.LOCK_UN
LOCK_NB = fcntl.LOCK_NB

def try_api(api_url):
        flog = open("log", "a+")
        while True:
                while True:
                        try:
                                fh = open("api_limit", "a+")
                                fcntl.flock(fh.fileno(), LOCK_EX|LOCK_NB)
                                break
                        except IOError:
                                flog.write("FILE's LOCKED,WAIT....{0}\n".format(time.ctime()))
                                fh.close()
                                time.sleep(1)

                if(fh.tell() == 0):
                        data = urllib.request.urlopen(api_url)
                        fh.write("{0},{1},{2}\n".format(time.ctime(), 1, int(time.time())))
                        flog.write("START at {0}\n".format(time.ctime()))
                        flog.write("cnt == 1\n")
                        break;

                os.lseek(fh.fileno(), -17, os.SEEK_END)
                lastline = fh.read(16)
                lasttime, cnt  = lastline.split(',')[-1:-3:-1] # get the last two element, cnt and lasttime 
                if(int(time.time()) - int(lasttime) >= 65):
                        cnt = 1
                        data = urllib.request.urlopen(api_url)
                        fh.write("{0},{1},{2}\n".format(time.ctime(), cnt, int(time.time())))
                        flog.write("START at {0}\n".format(time.ctime()))
                        flog.write("cnt == 1\n")
                        break
                elif int(cnt) >= 40:
                        flog.write("No More API at this time {0}\n".format(time.ctime()))
                        flog.write("END at {0}\n".format(time.ctime()))
                        fcntl.flock(fh.fileno(), LOCK_UN)
                        fh.close()
                        time.sleep(65)
                        #time.sleep(int(lasttime) + 65 - int(time.time()))
                else:
                        cnt = int(cnt)
                        cnt += 1
                        fh.write("{0},{1},{2}\n".format(time.ctime(),cnt, lasttime ))
                        flog.write("cnt == {0}\n".format(cnt))
                        data = urllib.request.urlopen(api_url)
                        break
        fcntl.flock(fh.fileno(), LOCK_UN)
        fh.close()
        flog.close()
        return data 
