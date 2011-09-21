#!/usr/bin/python3.1
import cgi, cgitb
import sys
form = cgi.FieldStorage()
arg1 = form.getvalue("arg1", "0")
arg2 = form.getvalue("arg2", "0")
print("Content-type:text/html\r\n\r\n")
#print("<html>")
#print("<head>")
#print("<title>Do_Func</title>")
#print("</head>")
#print("<body>")
#i = 0
#for i in range(1000000000000):
#        print("<h4>", i, "</h4>")
#print("</body>")
#print("</html>")
fh = open("ot2.html", "r",)
for line in fh.readlines():
        try:
                print(line.encode("utf8"))
        except:
                pass
