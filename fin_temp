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
                        if 'douban.com/group' in args[2]:
                                cmd = ' '.join(('python3.1', DO_CI_PATH))
                                print('run',cmd, time.ctime())
                                flog.write('[LOG]\t{0}:\t run cmd:{1} with args:\n'.format(time.ctime(), cmd, args))
                                flog.flush()
                                os.system(cmd)
                                longurl = HOSTNAME + 'history/' + args[-3].split('/')[-1]
                                cmd = ' '.join(('python2.6' , SEND_STATUS_PATH, 'm', args[-2], args[0], args[7], longurl))
                                                                        #opt, sid, send_to, content_url_short, content_url_long
                                print('run',cmd, time.ctime())
                                flog.write('[LOG]\t{0}:\t run cmd:{1}\n'.format(time.ctime(), cmd))
                                flog.flush()
                                #os.system(cmd)
                        else:
                                cmd = ' '.join(('python3.1', DO_2P_PATH))
                                print('run',cmd, time.ctime())
                                flog.write('[LOG]\t{0}:\t run cmd:{1} with args:\n'.format(time.ctime(), cmd, args))
                                flog.flush()
                                os.system(cmd)
                                longurl = HOSTNAME + 'history/' + args[-3].split('/')[-1]
                                cmd = ' '.join(('python2.6' , SEND_STATUS_PATH, 'm', args[-2], args[0], args[5], longurl))
                                print('run',cmd, time.ctime())
                                flog.write('[LOG]\t{0}:\t run cmd:{1}\n'.format(time.ctime(), cmd))
                                flog.flush()
                                #os.system(cmd)
                        user_queue.remove_first_user()
                else:
                        print('No User In Queue Now:(')
                        flog.write('[LOG]\t{0}:\t No User In Queue Now:(\n'.format(time.ctime()))
                        flog.flush()
                        time.sleep(30)

if __name__ == '__main__':
        main()
