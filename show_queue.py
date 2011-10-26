#!/usr/bin/env python2.6
# -*- coding: UTF-8 -*-

import cgi
import sys
import codecs
import pickle

cat_chs = {'movie':'电影','music':'音乐','book':'书籍'}

def main():
        # finish login process
        form = cgi.FieldStorage()
        sid = form.getvalue("oauth_token", None)
        key = None
        if sid != None:
                fp = open('./' + sid)
                data = pickle.load(fp)
                client = data[0]
                key = data[1]
                secret = data[2]
                fp.close()
                key, secret, uid = client.client.get_access_token(key, secret)
                if key:
                        client.client.login(key, secret)
                        fp = open('./_' + sid, 'w')
                        pickle.dump(client, fp)
                        fp.close()
        # finish login process
        fh = open('./wait_queue')
        lines = fh.readlines()
        fh.close()
        wait_nr = len(lines) - 1

        print "Content-type:text/html; charset=UTF-8\r\n\r\n"
        print '<html>'
        print '<head>'
        print '<meta http-equiv="content-type" content="text/html; charset=utf8">'
        print '<title>Waiting Line</title>'
        print '</head>'
        print '<body>'
        if key == None:
                print '<h2>授权登录失败!</h2>'
        else:
                print '<h2>授权登录成功!</h2>'
        print '<h2>当前有{0}位用户在您前面</h2>'.format(wait_nr)
        print '<div style="overflow-x: auto; overflow-y: auto; height: 400px; width:700px;">'
        print '<table id="table" border="1" align="center" width="700px" height="400px">'
        print '<tbody>'
        i = 1
        for line in lines:
                line = line.split('\t')
                print '<tr height="50px">\
                        <td width="50px">#{0}</td>\
                        <td width="100px"><a href="{1}">{2}</a></td>\
                        <td width="200px"><a href="{3}">{4}</a></td>\
                        <td width="50">{5}</td>\
                        <td width="50">{6}</td>\
                        </tr>'.format(i, 'http://www.douban.com/people/' + line[0], line[1], line[2], line[3], cat_chs[line[5]], line[4])
                i += 1
        print '</tbody></table></div></body></html>'

if __name__ == '__main__':
        main()
