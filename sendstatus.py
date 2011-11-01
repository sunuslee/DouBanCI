#!/usr/bin/python2.6
# -*- coding: UTF-8 -*-

import sys
import urllib
import pickle
import gdata
import html_parse
API_KEY = '053caab0d0224c680fb600127066e538'
SECRET = 'f2bebed97e85be8a'
IS_LOCAL = False
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

def saying(client, entry):
        res = client.AddBroadcasting('http://api.douban.com/miniblog/saying', entry)
        print 'saying finished'

def main():
        #       opt can be:
        #       'm' for mail
        #       's' for saying
        #       'sm' for mail and saying
        #       those 3 above and 1 type
        #       'g' for group
        #       't' for two people
        opt = sys.argv[1]
        sid = sys.argv[2]
        send_to = sys.argv[3]
        content_url_short = sys.argv[4]
        content_url_long = sys.argv[5]
        fp = open('./temp/' + sid)
        client = pickle.load(fp)
        fp.close()
        html_file_path = PAGEDIR + content_url_long.split('/')[-1]
        if 't' in opt:
                parse_result = html_parse.html_parse_t(html_file_path)
                uid     = parse_result[0]
                user2   = parse_result[1]
                rate_mv = parse_result[2]
                rate_mu = parse_result[3]
                rate_bk = parse_result[4]
        if 'm' in opt:
                subject = '来自DBCI的结果!'
                if 'g' in opt:
                        content = '''您好，访问以下地址获取您在DBCI提交的豆友共同喜好的搜索结果:)
                        {0}
                        希望您喜欢该APP
                        若短网址无法打开，请点击完整地址:
                        {1}'''.format(content_url_short, content_url_long)
                elif 't' in opt:
                        content = '''您好，访问以下地址获取您在DBCI提交的与{0}共同喜好的查询结果:)
                        {1}
                        希望您喜欢该APP
                        若短网址无法打开，请点击完整地址:
                        {2}'''.format(user2, content_url_short, content_url_long)
                sendmail(client, send_to, subject, content)
        if 's' in opt:
                if 'g' in opt:
                        parse_result = html_parse.html_parse_g(html_file_path)
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
                        content += '查看我们都喜欢什么{0}请点击{1}'.format(cat, content_url_short)
                elif 't' in opt:
                        content = '我和@{0}都有{1}部喜欢的电影，有{2}张喜欢的音乐，有{3}本喜欢的书'.format(uid, rate_mv, rate_mu, rate_bk)
                        content += '查看我们都喜欢什么请点击{0}'.format(content_url_short)

                content += '豆瓣喜爱，你也来试试吧!\n'
                entry = '''<?xml version='1.0' encoding='UTF-8'?>
                <entry xmlns:ns0="http://www.w3.org/2005/Atom" xmlns:db="http://www.douban.com/xmlns/">
                <content>{0}</content>
                </entry>'''.format(content)
                saying(client, entry)

if __name__ == '__main__':
        main()
