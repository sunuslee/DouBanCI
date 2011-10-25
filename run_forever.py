#!/usr/bin/env python2.6
# -*- coding: UTF-8 -*-

import user_queue
import os
import time
import url2

IS_LOCAL = False
ROOTDIR = "/home/sunus/apache/" if IS_LOCAL == True else "/usr/local/apache2/"
HOSTNAME = "http://localhost/"  if IS_LOCAL == True else "http://184.164.137.154/"
DO_CI_PATH = '/home/sunus/apache/cgi-bin/do_ci' if IS_LOCAL == True else '/usr/local/apache2/cgi-bin/do_ci'
SEND_MAIL_PATH = '/home/sunus/apache/cgi-bin/sendmail.py' if IS_LOCAL == True else '/usr/local/apache2/cgi-bin/sendmail.py'

API_KEY = '053caab0d0224c680fb600127066e538'
SECRET = 'f2bebed97e85be8a'
def main():
        while True:
                args = user_queue.fetch_user()
                if args != None:
                        suffix = str(int(time.time()))[-1:-9:-1]
                        longurl = HOSTNAME + "history/group_{0}_{1}_{2}.html".format(args[0], args[2].rsplit('/', 2)[1], suffix)
                        short_url = url2.get_shortenurl(longurl)
                        short_url = short_url.encode()
                        html_page_path = ROOTDIR + "htdocs/history/group_{0}_{1}_{2}.html".format(args[0], args[2].rsplit('/', 2)[1], suffix)
                        cmd = ' '.join(('python3.1', DO_CI_PATH, args[0], args[2], args[4], args[5], args[1], args[3], html_page_path, short_url))
                        print('run',cmd)
                        os.system(cmd)
                        send_to = args[0]
                        cmd = ' '.join(('python2.6' , SEND_MAIL_PATH, args[0], send_to, short_url))
                        print('run',cmd)
                        os.system(cmd)
                else:
                        print('No User In Queue Now:(')
                        time.sleep(60)

if __name__ == '__main__':
        main()
