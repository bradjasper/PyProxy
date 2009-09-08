import web
import urllib

AUTH_TOKEN = 'QWQ234klLQ@'

urls = (
    '/proxy/', 'proxy'
)

app = web.application(urls, globals())

class proxy:        

    def GET(self):

        url = web.input()['url']
        auth = web.input()['auth']

        assert auth == AUTH_TOKEN, "Invalid Auth Token"

        url = urllib.urlopen(url)
        contents = url.read()
        url.close()
        return contents
        

if __name__ == "__main__":
    app.run()
