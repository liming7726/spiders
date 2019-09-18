import time
from urllib.request import urlopen,Request
from urllib.parse import urlencode






def download(kw,page):
    url = 'http://tieba.baidu.com/f'
    params = {
        'kw': kw,
        'ie': 'utf-8',
        'pn': (page-1)*50
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    req = Request(url +'?'+urlencode(params), method='GET', headers=headers)
    # print(url + str(urlencode(params).encode('utf-8')))
    resp = urlopen(req)
    if resp.code == 200:
        bytes = resp.read()
        print(bytes)
        save(bytes,page)

def save(bytes,page):
    with open('python3_%s.html'%page, 'wb') as f:
        f.write(bytes)

if __name__ == '__main__':
    for page in range(1,6):
        print('开始下载%s'%page)
        download('李毅',page)

        time.sleep(3)

