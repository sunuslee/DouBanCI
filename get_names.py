import db_api
import urllib.request
import urllib.error
APIKEY = "053caab0d0224c680fb600127066e538"
def get_nickname(uid):
        try:
                fh = urllib.request.urlopen("http://api.douban.com/people/{0}?alt=atom&apikey={1}".format(uid,APIKEY))
                Content = fh.read().decode("utf8")
                fh.close()
        except (urllib.error.URLError, ValueError) as e:
                if hasattr(e, 'reason'):
                        print("<h4>{0}</h4>".format(e.reason))
                if hasattr(e, 'code'):
                        print("<h4>Return code:",e.code,"error</h4>")
                        print("<h4>This username/group may not exsit</h4>")
                return None
        for line in Content.splitlines():
                if "</title>" in line:
                        nikename = line[8:-8]
                        return nikename

def get_group_name(group_url):
        group_page = urllib.request.urlopen(group_url)
        content = group_page.read(2048).decode("utf8")
        for line in content.splitlines():
                if '<title>' in line:
                        group_page.close()
                        return line.split('>')[1].split('<')[0] #Group name may have WhiteSpace!

