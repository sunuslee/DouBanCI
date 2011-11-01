#!/usr/bin/env python3.1
# -*- coding: UTF-8 -*-

import sys
import pickle
import url3
RETFILE  = 'http://10.10.149.18/r/showresult.py?'
def main():
        print("Content-type:text/html; charset=UTF-8\r\n\r\n")
        print("<html>\n")
        print("<head>\n")
        print('<meta http-equiv="content-type" content="text/html; charset=utf8" />\n')
        print("<title>Verification</title>\n")
        print("</head>\n")
        print("<body>\n")
        redirect_code = sys.argv[1]
        if len(redirect_code) != 4:
                print("Wrong!") # It needs more argument verification
        else:
                print("I will redirect you to:\n")
                redirect_url = url3.get_longurl(RETFILE + redirect_code)
                try:
                        print('<script language="javascript" type="text/javascript">')
                        print('<!--')
                        print('location.replace("{0}")'.format(redirect_url))
                        print('// -->')
                        print('</script>')
                        sys.stdout.flush()
                except KeyError:
                        print("Wrong Redirect Code!")
        print("</body>\n")
        print("</html>")

if __name__ == '__main__':
        main()
