import atom
import gdata
import gdata.service
import douban.service
import urllib
import oauth
import douban.client


API_KEY = "053caab0d0224c680fb600127066e538"
SECRET = 'f2bebed97e85be8a'
client = douban.service.DoubanService(api_key=API_KEY, secret = SECRET)
client.client.login()
try:
        res = client.AddDoumail('http://api.douban.com/people/sunus', 'apitest', 'apitest')
except gdata.service.RequestError as err:
        print 'Got an ERROR'
        infos = err[0]['body']
        dm_token = infos.split('&')[0].split('=')[1]
        dm_url = infos.split(';')[1]
        print dm_url
        token_string = raw_input()
        try:
                res = client.AddCaptchaDoumail('http://api.douban.com/people/sunus', 'apitest', 'apitest', dm_token, token_string)
        except SyntaxError:
                pass
except SyntaxError:
        pass # safe
finally:
        print 'Done'
