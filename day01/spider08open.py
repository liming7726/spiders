import json
from urllib.request import HTTPHandler,HTTPCookieProcessor,ProxyHandler
from urllib.request import build_opener
from urllib.request import Request
from http.cookiejar import CookieJar
from urllib.parse import urlencode


def get_jd():
    url = 'http://www.jd.com/'
    req = Request(url)

    #生成opener对象
    httphandler = HTTPHandler()

    opener = build_opener(httphandler)

    resp = opener.open(req)

    if resp.code == 200:
        bytes = resp.read()
        print(bytes.decode('utf-8'))

#构建我们的opener,支持HTTP的请求和Cookie的处理
opener = build_opener(HTTPHandler(),
                      HTTPCookieProcessor(CookieJar()))
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.132 Safari/537.36',
    'X-Requested-with': 'XMLHttpRequest',
    'Referer': 'http://www.renren.com/'
}
def login():
    url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019821521164'
    data = {
        'email': '610039018@qq.com',
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': 1,
        'captcha': 'web_login',
        'password': '3fa5ee1cc182f47fe3103b6170aeeb2d3bd291e15a479a2700346e9cff084968',
        'rkey': '4dbb3a17871b6815976ebba83bb808c2'
    }
    req = Request(url,urlencode(data).encode('utf-8'),headers)
    resp = opener.open(req)
    if resp.code == 200:
        bytes = resp.read()
        resp_json = json.loads(bytes.decode('utf-8'))
        if resp_json.get('code'):
            get_profile()
        else:
            print('登陆失败！！！')
def get_profile():
    url = 'http://www.renren.com/958915617'
    resp = opener.open(url)
    print(resp.read().decode('utf-8'))



def proxy_get(url):
    opener = build_opener(HTTPHandler(),
                          HTTPCookieProcessor(CookieJar()),
                          ProxyHandler(proxies={'http':'39.137.69.7:8080'}))
    resp = opener.open(url)
    if resp.code == 200:
        bytes = resp.read()
        print(bytes)
        with open('a.html','wb') as f:
            f.write(bytes)



if __name__ == '__main__':
    proxy_get('http://sou.zhaopin.com/?jl=530&kw=python&kt=3')


