#!/usr/bin/env python3.1
# -*- coding: UTF-8 -*-

import cgi
import sys
import codecs

cat_chs = {'movie':'电影','music':'音乐','book':'书籍'}

def main():
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
