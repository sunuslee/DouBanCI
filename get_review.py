#!/usr/bin/env python3.1
# -*- coding: UTF-8 -*-

import urllib.parse
import urllib.request
def get_review(user_nickname, item_name):
#        print("search the review for {0} from:{1}".format(item_name, user_nickname))
        q = '来自' + user_nickname + ' ' + item_name + '的评论'
        q = q.encode('gbk')
        q = urllib.parse.quote(q)
        url = 'http://www.baidu.com/s?wd=' + q
        cont = urllib.request.urlopen(url).read().decode('gbk', 'ignore')       # ignore the shitty characters
        i = 1
        while i < 3:
                idx1 = cont.find('<table cellpadding="0" cellspacing="0" class="result" id="{0}" >'.format(i))
                if idx1 > 0:
                        idx2 = cont[idx1:].find('</a><br></font></td></tr></table>')
                        if idx2 > 0:
                                result = cont[idx1: idx1 + idx2]
                                review_url = result.split('href="')[1].split('"')[0]    # We only TRY to take the first 2 results
                                if 'douban.com/review' in review_url:                   # if this is the review, we return,if not.return None
 #                                       print("Got the result:", review_url)            # Can't find a better way at this moment
                                        return review_url
                i += 1
        return None
def test():
        get_review('Multivac', '绿灯侠')
        get_review('TORO VAN DARKO','疯狂愚蠢爱')
        get_review('陈小漠', '七宗罪')
        get_review('陈大漠', '七宗罪')
        get_review('handin', '洛杉矶之战')
        get_review('走路去南极', '洛杉矶之战')
        get_review('sunus', '社交网络')
        get_review('Y.B.', 'Python语言入门')
        get_review('davidkoree', 'Python语言入门')

test()

