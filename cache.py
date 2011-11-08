#!/usr/bin/env python3.1
# -*- coding: UTF-8 -*-

import time
status_chs = {"wishmovie":"想看",       "watchingmovie":"在看",         "watchedmovie":"看过",
              "wishmusic":"想听",       "listeningmusic":"在听",        "listenedmusic":"听过",
              "wishbook":"想读",        "readingbook":"在读",           "readbook":"读过"}

IS_LOCAL = False
ROOTDIR = "/home/sunus/apache/" if IS_LOCAL == True else "/usr/local/apache2/"
def write_entry(fh, entry_type, entry):
        fh.write('\t<{0}>{1}</{0}>\n'.format(entry_type, entry))

def cache_save(filename_path):
        filename = filename_path.split('/')[-1]
        rl = filename.rfind('_')
        rl = filename[:rl].rfind('_')
        user = filename[:rl]
        cat = filename.split('_')[-2]
        item_summary = "<summary>"
        item_status = "<db:status>"
        item_title = "<title>"
        item_id = "<id>"
        item_link = 'http://{0}.douban.com/subject'.format(cat)
        item_aka = '<db:attribute lang="zh_CN" name="aka">'
        item_rating = '<gd:rating'
        fw = open(ROOTDIR + r'/htdocs/cache_datas/' + 'cache_' + user + '_' + cat, 'w', encoding = 'utf8')
        file_idx = 1
        while True:
                try:
                        fr = open(filename_path, 'r', encoding = 'utf8')
                        content = fr.read()
                except IOError as e:
                        print('user:{0:20} {1:8} finished total:{2:4} \t{3}'.format(user, cat, file_idx, time.ctime()))
                        break
                in_entry = False
                for line in content.splitlines():
                        if "<entry>" in line:
                                in_entry = True
                                aka = '-1'
                                summary = '-1' 
                                rating = '-1' # those may NOT exist
                        if in_entry == True:
                                if item_summary in line:
                                        summary = line.split('>')[1].split('<')[0]
                                elif item_status in line:
                                        status = line.split('>')[1].split('<')[0]
                                        status = status_chs[status + cat]
                                elif item_id in line and cat in line:
                                        link = item_link + '/' + line.split('/')[-2][:-1]
                                elif item_title in line:
                                        title = line.split('>')[1].split('<')[0]
                                elif item_aka in line:
                                        aka = line.split('>')[1].split('<')[0]
                                elif item_rating in line:
                                        rating = line.split('value=')[1].split('"')[1]
                                elif "</entry>" in line:
                                        in_entry = False
                                        entry = '\t'.join((status, link, title, aka, rating, summary, '\n'))
                                        fw.write(entry)
                                else:
                                        pass
                file_idx += 50
                fp = ''
                for l in filename_path.split('_')[ : -1]:
                        fp += (l + '_')
                fp += str(file_idx)
                filename_path = fp
        fw.close()

def cache_load(filename_path):
        item_dict = {}
        fr = open(filename_path, 'r', encoding = 'utf8')
        content = fr.read()
        for line in content.splitlines():
                line = line.split('\t')
                item_dict[line[2]] = [line[0], line[1], line[3] if line[3] != '-1' else line[2] ,line[4],line[5]]
        fr.close()
        return item_dict

