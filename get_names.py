#!/usr/bin/env python2.6
# -*- coding: UTF-8 -*-
import httplib2
import urllib
import urllib2

'''
i don't know why this function can NOT WORK IN OAUTH.py!!
def get_nickname(uid):
        h = httplib2.Http("./.cache")
        next_line_is_nickname = False
        resp, cont = h.request('http://www.douban.com/people/' + uid)
        if resp['status'] == '200':
                cont = cont.decode('utf8')
                for line in cont.splitlines():
                        if '<title>' in line:
                                next_line_is_nickname = True
                        elif next_line_is_nickname == True:
                                nickname = line
                                return nickname
                return None
        return None
'''
def get_nickname(uid):
        next_line_is_nikename = False
        try:
                fh = urllib2.urlopen('http://www.douban.com/people/' + uid)
                cont = fh.read(512).decode('utf8')
                for line in cont.splitlines():
                        if '<title>' in line:
                                next_line_is_nikename = True
                        elif next_line_is_nikename == True:
                                nikename = line
                                return nikename
        except (urllib2.HTTPError, ValueError) as e:
                if hasattr(e, 'reason'):
                        print "<h4>{0}</h4>".format(e.reason) 
                if hasattr(e, 'code'):
                        print("<h4>Return code:",e.code,"error</h4>")
                print("<h4>This username/group may not exsit</h4>")
                return None
'''
def get_group_name(group_url):
        h = httplib2.Http("./.cache")
        resp, cont = h.request(group_url)
        if resp['status'] == '200':
                for line in cont.splitlines():
                        if '<title>' in line:
                                return line.split('>')[1].split('<')[0] #Group name may have WhiteSpace!
                return None
        return None
'''
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

def get_user_icon(uid):
        fh = urllib2.urlopen('http://www.douban.com/people/' + uid)
        cont = fh.read().decode('utf8')
        for line in cont.splitlines():
                if 'douban.com/icon' in line:
                        icon = line.split('"')[1]
                        return icon

def get_nickname_and_icon(uid):
        h = httplib2.Http("./.cache")
        next_line_is_nickname = False
        resp, cont = h.request('http://www.douban.com/people/' + uid)
        if resp['status'] == '200':
                cont = cont.decode('utf8')
                in_info = False
                for line in cont.splitlines():
                        if '<div id="db-usr-profile">' in line:
                                in_info = True
                        if in_info == True:
                                if '</div>' in line:
                                        return None
                                if 'douban.com/icon' in line:
                                        icon = line.split('"')[1]
                                        nickname = line.split('"')[3]
                                        return [icon, nickname]
        return None


def names_test():
        get_nickname_and_icon('aka')
        print "aka's nickname is"
        print get_nickname('aka')
        print "sunus's nickname is"
        print get_nickname('sunus')
        print get_user_icon('sunus')
        print get_user_icon('3215295')
        print get_user_icon('47844141')
        print "unknownsunus is nickname is,"
        print get_nickname('unknownsunus')
        print 'http://www.douban.com/group/zhuangb/'
        print get_group_name('http://www.douban.com/group/zhuangb/')
        print 'http://www.douban.com/group/The-Event/'
        print get_group_name('http://www.douban.com/group/The-Event/')
        print 'http://www.douban.com/group/yahooks/'
        print get_group_name('http://www.douban.com/group/yahooks/')
        print 'http://www.douban.com/group/yaho00ks/'
        print get_group_name('http://www.douban.com/group/yah00ks/')
