from http.client import HTTPResponse
from urllib.request import Request, urlretrieve, urlopen
from urllib.parse import urlencode


def get(url, params: dict = None, headers: dict = None) -> HTTPResponse:
    if params:
        parar_str = urlencode(params)
        subfix = '?' if url.find('?') == -1 else '' if url.find('=') == -1 else '&'
        url += subfix + parar_str
        print(url)
    if headers:
        req = Request(url,headers=headers)
    else:
        req = Request(url)

    return urlopen(req)


def save():
    def save(url, name=None, flage=False):
        img = urlopen(url)
        if img.code == 200:
            bytes = img.read()
            with open('sucai/%s.jpg' % name, 'wb') as f:
                f.write(bytes)

def post():
    pass