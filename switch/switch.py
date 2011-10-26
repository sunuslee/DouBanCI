#!/usr/bin/env python

# Using the program to switch the DBCI running enviorment
# this file should be with those cgi files
# run './switch.py s' on the server
# run './switch.py l' on the localhost

import sys
import os

def main():
        opt = sys.argv[1]
        if opt.lower() == 'l':
                patten = 'IS_LOCAL = False'
                val    = 'IS_LOCAL = True'
        elif opt.lower() == 's':
                patten = 'IS_LOCAL = True'
                val    = 'IS_LOCAL = False'
        else:
                print 'Wrong argument!'
                return
        files = os.listdir('.')
        for cur_file in files:
                found = False
                if cur_file != __file__:
                        fw = open('fin_temp', 'w')
                        fr = open(cur_file)
                        i = 0
                        lines = fr.readlines()
                        for line in lines:
                                if found == False and patten in line:
                                        found = True
                                        print 'Found line',line,__file__
                                        lines[i] = val + '\n'
                                i += 1
                        fw.writelines(lines)
                        fw.close()
                        fr.close()
                        if found == True:
                                fr = open('fin_temp')
                                fw = open(cur_file, 'w')
                                fw.writelines(fr.readlines())
                                fw.close()
                                fr.close()
main()
