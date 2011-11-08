#!/usr/bin/env python2.6
# -*- coding: UTF-8 -*-

import user_queue
import os
import time
import url2
import pickle

IS_LOCAL = False
ROOTDIR = "/home/sunus/apache/" if IS_LOCAL == True else "/usr/local/apache2/"
HOSTNAME = "http://10.10.149.18/"  if IS_LOCAL == True else "http://184.164.137.154/"
DO_CI_PATH = '/home/sunus/apache/cgi-bin/do_ci' if IS_LOCAL == True else '/usr/local/apache2/cgi-bin/do_ci'
DO_2P_PATH = '/home/sunus/apache/cgi-bin/do_2people' if IS_LOCAL == True else '/usr/local/apache2/cgi-bin/do_2people'
SEND_STATUS_PATH = '/home/sunus/apache/cgi-bin/sendstatus.py' if IS_LOCAL == True else '/usr/local/apache2/cgi-bin/sendstatus.py'

API_KEY = '053caab0d0224c680fb600127066e538'
SECRET = 'f2bebed97e85be8a'
flog = open('run_log', 'a')
def main():
        while True:
                args = user_queue.fetch_user()
                if args != None:
                        cmd = ' '.join(('python3.1', DO_CI_PATH))
                        print('run',cmd, time.ctime())
                        flog.write('[LOG]\t{0}:\t run cmd:{1} with args:\n'.format(time.ctime(), cmd, args))
                        flog.flush()
                        os.system(cmd)
                        user_queue.remove_first_user()
                        time.sleep(15)
                else:
                        print('No User In Queue Now:(')
                        flog.flush()
                        time.sleep(30)

if __name__ == '__main__':
        main()
