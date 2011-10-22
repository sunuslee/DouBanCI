#!/usr/bin/env python3.1
# -*- coding: UTF-8 -*-

import user_queue
import os
import time
import sendmail
def mian():
        while True:
                args = user_queue.fetch_user()
                if args != None:
                        cmd = ' '.join(('python3.1', DO_CI_PATH, args[0], args[2],args[4], args[5]))
                        os.system(cmd)
                        sendmail.sendmail(args[0], 'notify', 'content')
                else:
                        time.sleep(60)

if __name__ == '__main__':
        main()
