#!/usr/bin/env python2.6
# -*- coding: UTF-8 -*-

import os
import fcntl
import random
import time
import get_names
LOCK_EX = fcntl.LOCK_EX
LOCK_UN = fcntl.LOCK_UN
LOCK_NB = fcntl.LOCK_NB

def fetch_user():
        while True:
                try:
                        fh = open("./wait_queue", "r")
                        fcntl.flock(fh.fileno(), LOCK_EX|LOCK_NB)
                        first_line = fh.readline()
                        first_line = first_line[0:-1] #remove the last '\n'
                        if first_line == '': #empty file
                                return None
                        fcntl.flock(fh.fileno(), LOCK_UN)
                        fh.close()
                        return first_line.split('\t') #remove '\t'
                except IOError:
                        fh.close()

# the first line will never be ''
def remove_first_user():
        while True:
                try:
                        fh = open("./wait_queue", "r+")
                        fcntl.flock(fh.fileno(), LOCK_EX|LOCK_NB)
                        first_line = fh.readline()
                        rest_queue = fh.readlines()
                        os.lseek(fh.fileno(), 0, os.SEEK_SET)
                        fh.truncate(0)
                        fh.writelines(rest_queue)
                        fcntl.flock(fh.fileno(), LOCK_UN)
                        fh.close()
                        return 
                except IOError:
                        fh.close()

# add a user into wait_queue and return it's user_nr
def add_user(user):
        user = user.encode('utf8')
        while True:
                try:
                        fh = open('./wait_queue', 'a+')
                        fcntl.flock(fh.fileno(), LOCK_EX|LOCK_NB)
                        if os.path.getsize('./wait_queue') == 0:
                                nr = 1
                        else:
                                os.lseek(fh.fileno(), -8, os.SEEK_END)
                                nr = fh.read(7)
                                nr = int(nr) + 1
                        user = user + '\t{0:7}\n'.format(nr)
                        fh.write(user)
                        fcntl.flock(fh.fileno(), LOCK_UN)
                        fh.close()
                        return nr
                except IOError:
                        fh.close()

# This function returns the number of how many user are waiting befor user #x
# get serviced.
def get_wait_user_nr(user_x):
        fh = open('./wait_queue')
        first_nr = fh.readline()
        first_nr = first_nr.split()[-1]
        first_nr = int(first_nr)
        nr = int(user_x) - first_nr
        if nr >= 0:
                return nr
        else:
                return -1
'''
group_addrs = ('http://www.douban.com/group/zhuangb/',
                'http://www.douban.com/group/tjpu/',
                'http://www.douban.com/group/kaopulove/',
                'http://www.douban.com/group/python/',
                'http://www.douban.com/group/geek_wife/',
                'http://www.douban.com/group/ai_Junko/',
                'http://www.douban.com/group/nasha/',
                'http://www.douban.com/group/Yi-club/',
                'http://www.douban.com/group/yahooks/')
uids = ('sunus',
        'aka',
        'zhuzailing',
        '47844141',
        '3215295',
        'hongqn',
        'ahbei',
        'kingsamchen',
        '50865285',
        '3146104')

charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def get_randstr(length):
        randstr = []
        while length:
                randstr.append(charset[random.randint(0,61)])
                length -= 1
        randstr = ''.join(randstr)
        return randstr

def test_queue():
        pid = os.fork()
        if pid == 0:
                while True:
                        sleep_time = random.randint(0,2)
                        uid = uids[random.randint(0, 9)]
                        location = get_randstr(8)
                        group_addr = group_addrs[random.randint(0, 8)]
                        cat = ('movie','music','book')[random.randint(0, 2)]
                        anonymous = random.randint(0,1)
                        nickname = get_names.get_nickname(uid)
                        group_name = get_names.get_group_name(group_addr)
                        entry = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format(uid, nickname, group_addr, group_name, location, cat, anonymous)
                        add_user(entry)
                        time.sleep(sleep_time)
        else:
                while True:
                        sleep_time = random.randint(0,5)
                        user_info = fetch_user()
                        time.sleep(sleep_time)


def test_add_user():
        username = get_randstr(16)
        group_addr = group_addrs[random.randint(0,8)]
        location = get_randstr(8)
        cat = ('movie','music','book')[random.randint(0,2)]
        anonymous = random.randint(0,1)
        entry = "{0}\t{1}\t{2}\t{3}\t{4}".format(username, group_addr, location, cat, anonymous)
        add_user(entry)

DO_CI_PATH = '/home/sunus/apache/cgi-bin/do_ci'
def test_fet_user():
        args = fetch_user()
        cmd = ' '.join(('python3.1', DO_CI_PATH, args[0], args[2],args[4], args[5], args[1], args[3]))
        print(cmd)
        os.system(cmd)
'''
