#!/usr/bin/env python3.1

status_chs = {"wishmovie":"想看",       "watchingmovie":"在看",         "watchedmovie":"看过",
              "wishmusic":"想听",       "listeningmusic":"在听",        "listenedmusic":"听过",
              "wishbook":"想读",        "readingbook":"在读",           "readbook":"读过"}

def write_entry(fh, entry_type, entry):
        fh.write('\t<{0}>{1}</{0}>\n'.format(entry_type, entry))

def cache_save(filename_path):
        filename = filename_path.split('/')[-1]
        user = filename.split('_')[0]
        cat = filename.split('_')[1]
        item_status = "<db:status>"
        item_title = "<title>"
        item_id = "<id>"
        item_link = 'http://{0}.douban.com/subject'.format(cat)
        item_aka = '<db:attribute lang="zh_CN" name="aka">'
        fw = open('cache_' + user + '_' + cat, 'w')
        file_idx = 1
        while True:
                try:
                        fr = open(filename_path)
                        content = fr.read()
                except IOError as e:
                        print('err', e)
                        break
                step = 1
                for lines in content.splitlines():
                        if step == 1 and item_status in lines:
                                status = lines[13:-12]
                                step = 2
                                fw.write(status_chs[status + cat] + '\t')
                        elif step == 2 and item_id in lines:
                                link = item_link + '/' + lines.strip()[3:-5].split('/')[-1]
                                fw.write(link + '\t')
                                step = 3
                        elif step == 3 and item_title in lines:
                                title = lines[10:-8]
                                step = 4
                                fw.write(title + '\t')
                        #in case the item DOESN NOT HAVE A AKA
                        elif step == 4 and item_aka in lines:
                                aka = lines[41: -15]
                                step = 1
                                fw.write(aka + '\t')
                        elif "</entry>" in lines:
                                step = 1
                                fw.write('\n')
                file_idx += 50
                fp = ''
                for l in filename_path.split('_')[ : -1]:
                        fp += (l + '_')
                fp += str(file_idx)
                filename_path = fp
        fw.close()

def cache_load(filename_path):
        item_dict = {}
        fr = open(filename_path)
        content = fr.read()
        for line in content.splitlines():
                line = line.split('\t')
                item_dict[line[2]] = [line[0], line[1], line[3] if len(line) == 5 else 'None']
        fr.close()
        return item_dict

cache_save('./34403969_movie_1')
cache_load('./cache_34403969_movie')
