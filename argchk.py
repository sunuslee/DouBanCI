#!/usr/bin/env python2.6
# -*- coding: UTF-8 -*-

import base64
import urllib2
IS_LOCAL = True
HOSTNAME = "http://10.10.149.18/"  if IS_LOCAL == True else "http://184.164.137.154/"
def exp_check(you, exp_code):
        if you == None or exp_code == None:
                return False
        you = you[::-1]
        b64s_you = base64.encodestring(you)
        b64s_you = b64s_you[:3]
        if b64s_you == exp_code:
                return True
        else:
                print "<h2>Sorry:(</h2>"
                print "<h2>This page is now only for testing users only</h2>"
                print "<h2>you:{0}<br>code:{1}".format(you[::-1], exp_code)
                return False
def arg_chk_repeat(uid):
        fq = open('wait_queue')
        for line in fq.readlines():
                if uid == line.split('\t')[0]:
                        print '<h4>请误重复提交请求，等您收到当前请求的结果后即可继续使用本应用。谢谢！</h4>'
                        fq.close()
                        return True
        fq.close()
        return False

def arg_chk(user, group = None, location = None):
        if group is None:
                print("<h4>搜索小组不能为空！</h4>")
                return False
        if location is None:
                print("<h4>搜索地区不能为空！</h4>")
                return False
        try:
                urllib2.urlopen("http://www.douban.com/people/{0}".format(user))
                if "http://www.douban.com/group/" not in group:
                        raise urllib2.URLError('Wrong URL')
                urllib2.urlopen(group)
                return True
        except urllib2.URLError as e:
                if hasattr(e, 'code') or e.reason == 'Wrong URL':
                        print '<h4>请检查小组的地址及用户ID是否正确，正确的小组地址格式如下：</h4><br>'
                        print '<a href="http://www.douban.com/group/tjpu/">http://www.douban.com/group/tjpu/</a><br>'
                        print '<a href="http://www.douban.com/group/183492/">http://www.douban.com/group/183492/</a><br>'
                        print '<h4>正确的用户ID格式如下（数字或字母形式都可）<br>'
                        print '如果你的豆瓣主页地址为（数字形式）：<a href="{0}">{0}</a><br>'.format('http://www.douban.com/people/3146104/')
                        print '则填写：3146104<br>'
                        print '如果你的豆瓣主页地址为（字母形式）：<a href="{0}">{0}</a><br>'.format('http://www.douban.com/people/sunus/')
                        print '则填写: sunus<br>'
                        print '<br><a href="{0}">点击返回修改</a>'.format(HOSTNAME)
                elif hasattr(e, 'reason'):
                        print '<h4>当前网络出问题了......</h4>'
                return False

def arg_chk2p(user1, user2):
        try:
                urllib2.urlopen("http://www.douban.com/people/{0}".format(user1))
                urllib2.urlopen("http://www.douban.com/people/{0}".format(user2))
                return True
        except urllib2.URLError as e:
                if hasattr(e, 'code'):
                        print '<h4>请检查用户ID是否正确'
                        print '<h4>正确的用户ID格式如下（数字或字母形式都可）<br>'
                        print '如果你的豆瓣主页地址为（数字形式）：<a href="{0}">{0}</a><br>'.format('http://www.douban.com/people/3146104/')
                        print '则填写：3146104<br>'
                        print '如果你的豆瓣主页地址为（字母形式）：<a href="{0}">{0}</a><br>'.format('http://www.douban.com/people/sunus/')
                        print '则填写: sunus<br>'
                        print '<br><a href="{0}">点击返回修改</a>'.format(HOSTNAME)
                elif hasattr(e, 'reason'):
                        print '<h4>当前网络出问题了......</h4>'
                return False
def test():
        print arg_chk('sunuss', 'http://www.douban.com/gr0up/python', 'bj')
        print arg_chk('sunus', 'python', 'bj')
        print arg_chk('sunus', 'http://www.douban.com/group/pyth0n', 'bj')
        print exp_check('sunus', 'c3V')
        print exp_check('47844141', 'lol')
        print exp_check('3146014', 'MzE')
        print exp_check('3146014', 'MZE')

#test()
