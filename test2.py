#!/usr/bin/python3.1
# -*- coding: UTF-8 -*-

import sys
import time
def main():
        url = 'http://www.baidu.com'
        print("Content-type:text/html; charset=UTF-8\r\n\r\n")
        print("<html>\n")
        print("<head>\n")
        print('<meta http-equiv="content-type" content="text/html; charset=utf8" />\n')
        print("<title>Verification test</title>\n")
        print("</head>\n")
        print("<body>\n")
        print('hello this is 1st line\n')
        sys.stdout.flush()
        print('<script language="javascript" type="text/javascript">')
        print('<!--')
        print('window.open("{0}", "newwindow","height=480, width=640, top=0, left=0,toolbar=no, menubar=no,resizable=yes,status=no")'.format(url))
        print('// -->')
        print('</script>')
        time.sleep(15)
        print('I AM THE FUCKING 2ND LINE!')
        print('</body>\n')
        print('</html>\n')

if __name__ == '__main__':
        main()
