#!/usr/bin/env python3.1
# -*- coding: UTF-8 -*-

import time
import threading
import queue
import fcntl
import time
import random
LOCK_EX = fcntl.LOCK_EX
LOCK_UN = fcntl.LOCK_UN
LOCK_NB = fcntl.LOCK_NB
class Worker(threading.Thread):

        def __init__(self, work_queue):
                super().__init__()
                self.work_queue = work_queue
        def run(self):
                while True:
                        try:
                                arg = self.work_queue.get()
                                self.process(arg, self.getName())
                        finally:
                                self.work_queue.task_done()
        
        def process(self, arg, name):
                func(arg, name)

def func(arg, name):
        while True:
                try:
                        fh = open("mt", "a+")
                        fcntl.flock(fh, LOCK_EX|LOCK_NB)
                        break
                except IOError:
                        fh.close()
        r = random.randint(0, 5)
        info = "{0:<32} {1:<32} {2:<32} run {0}secs\n".format(arg, name, time.ctime(), r)
        print(info)
        fh.write(info)
        time.sleep(2)
        fcntl.flock(fh, LOCK_UN)
        fh.close()


def main():
        # THREAD PART
        q = queue.Queue()
        for i in range(5):
                worker = Worker(q)
                worker.daemon = True
                worker.start()
        for i in range(90):
                q.put(i)
        q.join()
        # THREAD PART
        print("done")

if __name__ == "__main__":
        main()
