import urllib.request
import urllib.error

def get_nickname(uid):
        next_line_is_nikename = False
        try:
                fh = urllib.request.urlopen('http://www.douban.com/people/' + uid)
                cont = fh.read(512).decode('utf8')
                for line in cont.splitlines():
                        if '<title>' in line:
                                next_line_is_nikename = True
                        elif next_line_is_nikename == True:
                                nikename = line
                                return nikename
        except (urllib.error.URLError, ValueError) as e:
                if hasattr(e, 'reason'):
                        print("<h4>{0}</h4>".format(e.reason))
                if hasattr(e, 'code'):
                        print("<h4>Return code:",e.code,"error</h4>")
                        print("<h4>This username/group may not exsit</h4>")
                return None


def get_group_name(group_url):
        try:
                group_page = urllib.request.urlopen(group_url)
                content = group_page.read(512).decode("utf8")
                for line in content.splitlines():
                        if '<title>' in line:
                                group_page.close()
                                return line.split('>')[1].split('<')[0] #Group name may have WhiteSpace!
        except (urllib.error.URLError, ValueError) as e:
                if hasattr(e, 'reason'):
                        print("<h4>{0}</h4>".format(e.reason))
                if hasattr(e, 'code'):
                        print("<h4>Return code:",e.code,"error</h4>")
                        print("<h4>This username/group may not exsit</h4>")
                return None


def names_test():
        print("aka's nikename is", get_nickname('aka'))
        print("sunus's nikename is", get_nickname('sunus'))
        print("unknownsunus is nikename is,", get_nickname('unknownsunus'))
        print('group', 'http://www.douban.com/group/zhuangb/', get_group_name('http://www.douban.com/group/zhuangb/'))
        print('group', 'http://www.douban.com/group/The-Event/', get_group_name('http://www.douban.com/group/The-Event/'))
        print('group', 'http://www.douban.com/group/yahooks/', get_group_name('http://www.douban.com/group/yahooks/'))
        print('group', 'http://www.douban.com/group/yaho00ks/', get_group_name('http://www.douban.com/group/yah00ks/'))
