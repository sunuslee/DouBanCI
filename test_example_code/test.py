#!/usr/bin/python2.6
# -*- coding: UTF-8 -*-

import sys
import atom
import gdata
import gdata.service
import service
import urllib
import oauth
import client
import optparse

API_KEY = '053caab0d0224c680fb600127066e538'
SECRET = 'f2bebed97e85be8a'


def sendmail(send_to, subject, content):
        client = service.DoubanService(api_key=API_KEY, secret = SECRET)
        client.client.login()
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
                        res = client.AddCaptchaDoumail('http://api.douban.com/people/' + send_to, 'apitest', 'apitest', dm_token, token_string)
                except SyntaxError:
                        pass
        except SyntaxError:
                pass # safe
        finally:
                print 'Done'

def main():
        send_to = 'sunus'
        content_url = 'sunus_url'
        subject = '来自DBCI的结果!'
        content = '您好，访问以下网址获取您在DBCI提交的豆友共同喜好的搜索结果:)\n{0}\n希望您喜欢该APP\n'.format(content_url)
        print("Content-type:text/html; charset=UTF-8\r\n\r\n")
        print("<html>\n")
        print("<head>\n")
        print('<meta http-equiv="content-type" content="text/html; charset=utf8" />\n')
        print("<title>Verification test</title>\n")
        print("</head>\n")
        print("<body>\n")
        print('hello\n')
        sendmail(send_to, subject, content)
        print('</body>\n')
        print('</html>\n')

if __name__ == '__main__':
        main()
