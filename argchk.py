#!/usr/bin/env python2.6
# -*- coding: UTF-8 -*-

import base64
import urllib2
IS_LOCAL = True
HOSTNAME = "http://10.10.149.18/"  if IS_LOCAL == True else "http://184.164.137.154/"
def exp_check(you, exp_code):
        if you == None or exp_code == None:
                return False
        b64s_you = base64.encodestring(you)
        b64s_you = b64s_you[:3]
        if b64s_you == exp_code:
                return True
        else:
                return False

def arg_chk(user, group = None, location = None):
        if location is None:
                print("<h4>搜索地址不能为空！</h4>")
                return False
        try:
                urllib2.urlopen("http://www.douban.com/people/{0}".format(user))
                urllib2.urlopen(group)
                return True
        except (urllib2.URLError, ValueError) as e:
                if hasattr(e, 'reason'):
                        print 'Error!'
                if hasattr(e, 'code'):
                        print '<h4>请检查小组的地址及用户ID是否正确，正确的小组地址格式如下：</h4><br>'
                        print '<a href="http://www.douban.com/group/tjpu/">http://www.douban.com/group/tjpu/</a><br>'
                        print '<a href="http://www.douban.com/group/183492/">http://www.douban.com/group/183492/</a><br>'
                        print '<h4>正确的用户ID格式如下（数字或字母形式都可）<br>'
                        print '如果你的豆瓣主页地址为（数字形式）：<a href="{0}">{0}</a><br>'.format('http://www.douban.com/people/3146104/')
                        print '则填写：3146104<br>'
                        print '如果你的豆瓣主页地址为（字母形式）：<a href="{0}">{0}</a><br>'.format('http://www.douban.com/people/sunus/')
                        print '则填写: sunus<br>'
                        print '<br><a href="{0}">点击返回修改</a>'.format(HOSTNAME)
                return False

def test():
        print arg_chk('sunuss', 'http://www.douban.com/group/python', 'bj')
        print arg_chk('sunus', 'python', 'bj')
        print arg_chk('sunus', 'http://www.douban.com/group/pyth0n', 'bj')
        print exp_check('sunus', 'c3V')
        print exp_check('47844141', 'lol')
        print exp_check('3146014', 'MzE')
        print exp_check('3146014', 'MZE')

#test()
