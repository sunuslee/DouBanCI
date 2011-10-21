#!/usr/bin/env python3.1
# -*- coding: UTF-8 -*-
import cgi
import user_queue
import sys
import codecs
import get_names
cat_chs = {'movie':'电影','music':'音乐','book':'书籍'}
def main():
        global cat_chs
        form = cgi.FieldStorage()
        you = form.getvalue("you", "sunus")
        group_url = form.getvalue("group_url", "http://www.douban.com/group/python/")
        if group_url.endswith('/') == False:
                group_url += '/'
        location = form.getvalue("location", "天津")
        cat = form.getvalue("cat", "movie")
        anonymous = 0
        nickname = get_names.get_nickname(you)
        group_name = get_names.get_group_name(group_url)
        entry = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format(you, nickname, group_url, group_name, location, cat, anonymous)
        user_queue.add_user(entry)
        sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer) # comment this out if you want to debug

        fh = open('./wait_queue', encoding = 'utf8')
        lines = fh.readlines()
        fh.close()
        wait_nr = len(lines) - 1

        print("Content-type:text/html; charset=UTF-8\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<meta http-equiv="content-type" content="text/html; charset=utf8">')
        print('<title>Waiting Line</title>')
        print('</head>')
        print('<body>')
        print('<h2>当前有{0}位用户在您前面</h2>'.format(wait_nr))
        print('<div style="overflow-x: auto; overflow-y: auto; height: 400px; width:700px;">')
        print('<table id="table" border="1" align="center" width="700px" height="400px">')
        print('<tbody>')
        i = 1
        for line in lines:
                line = line.split('\t')
                print('<tr height="50px">\
                        <td width="50px">#{0}</td>\
                        <td width="100px"><a href="{1}">{2}</a></td>\
                        <td width="200px"><a href="{3}">{4}</a></td>\
                        <td width="50">{5}</td>\
                        <td width="50">{6}</td>\
                        </tr>'.format(i, 'http://www.douban.com/people/' + line[0], line[1], line[2], line[3], cat_chs[line[5]], line[4]))
                i += 1
        print('</tbody></table></div></body></html>')

if __name__ == '__main__':
        main()
