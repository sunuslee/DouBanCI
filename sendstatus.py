#!/usr/bin/python2.6
# -*- coding: UTF-8 -*-

import sys
import urllib
import pickle
import gdata
import html_parse

API_KEY = '053caab0d0224c680fb600127066e538'
SECRET = 'f2bebed97e85be8a'
IS_LOCAL = True
PAGEDIR = "/home/sunus/apache/htdocs/history/" if IS_LOCAL == True else "/usr/local/apache2/htdocs/history/"

def sendmail(client, send_to, subject, content):
        try:
                res = client.AddDoumail('http://api.douban.com/people/' + send_to, subject, content)
        except gdata.service.RequestError as err:
                print 'Got an ERROR'
                infos = err[0]['body']
                dm_token = infos.split('&')[0].split('=')[1]
                dm_url = infos.split(';')[1]
                print dm_url
                token_string = raw_input()
                try:
                        res = client.AddCaptchaDoumail('http://api.douban.com/people/' + send_to, subject, content, dm_token, token_string)
                except SyntaxError:
                        pass
        except SyntaxError:
                pass # safe
        finally:
                print 'mail sent'

def saying(client, html_file_path, short_url):
        parse_result = html_parse.html_parse(html_file_path)
        group_name = parse_result[0][0]
        location   = parse_result[0][1]
        cat        = parse_result[0][2]
        content = '缘分啊！我在 {0} 找到了在 {1} 喜欢 {2}的豆友，并且我们都有喜欢的{2}耶:'.format(group_name, location, cat)
        top_user_nr = 3 if len(parse_result[1]) >= 3 else len(parse_result[1])
        i = 0
        while i < top_user_nr:
                if parse_result[1][i][1] != 0:
                        content += '(@{0}:{1}项) '.format(*parse_result[1][i])
                i += 1
        content += '查看我们都喜欢什么{0}请点击{1}'.format(cat, short_url)
        content += '豆瓣喜爱，你也来试试吧!\n'
        entry = '''<?xml version='1.0' encoding='UTF-8'?>
        <entry xmlns:ns0="http://www.w3.org/2005/Atom" xmlns:db="http://www.douban.com/xmlns/">
        <content>{0}</content>
        </entry>'''.format(content)
        res = client.AddBroadcasting('http://api.douban.com/miniblog/saying', entry)
        print 'saying finished'

def main():
        #       opt can be:
        #       'm' for mail
        #       's' for saying
        #       'sm' for mail and saying
        opt = sys.argv[1]
        sid = sys.argv[2]
        send_to = sys.argv[3]
        content_url_short = sys.argv[4]
        content_url_long = sys.argv[5]
        fp = open('./temp/' + sid)
        client = pickle.load(fp)
        fp.close()
        if 'm' in opt:
                subject = '来自DBCI的结果!'
                content = '''您好，访问以下网址获取您在DBCI提交的豆友共同喜好的搜索结果:)
                {0}
                希望您喜欢该APP
                若短网址无法打开，请点击完整地址:
                {1}'''.format(content_url_short, content_url_long)

                sendmail(client, send_to, subject, content)
        if 's' in opt:
                html_file_path = PAGEDIR + content_url_long.split('/')[-1]
                saying(client, html_file_path, content_url_short)

if __name__ == '__main__':
        main()
