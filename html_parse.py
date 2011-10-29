#!/usr/bin/env python2.6
# -*- coding: UTF-8 -*-

def html_parse(file_path):
        f = open(file_path)
        rank = []
        for line in f.readlines():
                if '<!-- saying' in line:
                        line_split = line.split('\t')
                        if 'saying:glc' in line:
                                group_name = line_split[1]
                                location   = line_split[2]
                                cat        = line_split[3]
                        elif 'saying:rank' in line:
                                rank.append((line_split[2], line_split[3]))
        f.close()
        return ((group_name, location, cat), rank)

def test():
        res = html_parse('./test_page.html')
        print res
