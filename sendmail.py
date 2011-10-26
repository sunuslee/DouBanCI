#!/usr/bin/python2.6
# -*- coding: UTF-8 -*-

import sys
import urllib
import pickle
import gdata

API_KEY = '053caab0d0224c680fb600127066e538'
SECRET = 'f2bebed97e85be8a'
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
                print 'Done'

def main():
        sid = sys.argv[1] 
        send_to = sys.argv[2]
        content_url = sys.argv[3]
        subject = '来自DBCI的结果!'
        content = '您好，访问以下网址获取您在DBCI提交的豆友共同喜好的搜索结果:)\n{0}\n希望您喜欢该APP\n'.format(content_url)
        sid = raw_input('input the sid filename:')
        fp = open('./' + sid)
        client = pickle.load(fp)
        sendmail(client, send_to, subject, content)
if __name__ == '__main__':
        main()
