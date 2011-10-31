#!/usr/bin/env python2.6
# -*- coding: UTF-8 -*-

import urllib2

def get_nickname(uid):
        next_line_is_nickname = False
        try:
                fh = urllib2.urlopen('http://www.douban.com/people/' + uid)
                cont = fh.read(512).decode('utf8')
                for line in cont.splitlines():
                        if '<title>' in line:
                                next_line_is_nickname = True
                        elif next_line_is_nickname == True:
                                nickname = line
                                return nickname
        except (urllib2.HTTPError, ValueError) as e:
                if hasattr(e, 'reason'):
                        print("<h4>{0}</h4>".format(e.reason))
                if hasattr(e, 'code'):
                        print("<h4>Return code:",e.code,"error</h4>")
                        print("<h4>This username/group may not exsit</h4>")
                return None


def get_group_name(group_url):
        try:
                group_page = urllib2.urlopen(group_url)
                content = group_page.read(512).decode("utf8")
                for line in content.splitlines():
                        if '<title>' in line:
                                group_page.close()
                                return line.split('>')[1].split('<')[0] #Group name may have WhiteSpace!
        except (urllib2.HTTPError, ValueError) as e:
                if hasattr(e, 'reason'):
                        print("<h4>{0}</h4>".format(e.reason))
                if hasattr(e, 'code'):
                        print("<h4>Return code:",e.code,"error</h4>")
                        print("<h4>This username/group may not exsit</h4>")
                return None


def names_test():
        print "aka's nickname is"
        print get_nickname('aka')
        print "sunus's nickname is"
        print get_nickname('sunus')
        print "unknownsunus is nickname is,"
        print get_nickname('unknownsunus')
        print 'http://www.douban.com/group/zhuangb/'
        print get_group_name('http://www.douban.com/group/zhuangb/')
        print 'http://www.douban.com/group/The-Event/'
        print get_group_name('http://www.douban.com/group/The-Event/')
        print 'http://www.douban.com/group/yahooks/'
        print get_group_name('http://www.douban.com/group/yahooks/')
        print 'http://www.douban.com/group/yaho00ks/', 
        print get_group_name('http://www.douban.com/group/yah00ks/')
