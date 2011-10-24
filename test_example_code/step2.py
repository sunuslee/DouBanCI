#!/usr/bin/python2.6
# -*- encoding:utf-8 -*-

import cgi
import pickle
import sendmail
def main():
        form = cgi.FieldStorage()
        sid = form.getvalue("sid", None)
        print("Content-type:text/html; charset=UTF-8\r\n\r\n")
        print("<html>\n")
        print("<head>\n")
        print('<meta http-equiv="content-type" content="text/html; charset=utf8" />\n')
        print("<title>NEXT STEP</title>\n")
        print("</head>\n")
        print("<body>\n")
        print(sid)
        fp = open('./' + sid)
        data = pickle.load(fp)
        client = data[0]
        key = data[1]
        secret = data[2]
        fp.close()
        print('O_key:', key)
        print('O_secret:', secret)
        key, secret, uid = client.client.get_access_token(key, secret)
        print('key:', key)
        print('secret:', secret)
        print('uid:', uid)
        if key:
                client.client.login(key, secret)

        print("</body>")
        print("</html>")

if __name__ == "__main__":
        main()

