#!/usr/bin/env python2.6

import base64

def exp_check(you, exp_code):
        if you == None or exp_code == None:
                return False
        b64s_you = base64.encodestring(you)
        b64s_you = b64s_you[:3]
        if b64s_you == exp_code:
                return True
        else:
                return False

def test():
        print exp_check('sunus', 'c3V')
        print exp_check('47844141', 'lol')
        print exp_check('3146014', 'MzE')
        print exp_check('3146014', 'MZE')

#test()
