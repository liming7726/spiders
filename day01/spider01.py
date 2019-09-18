import re
import urllib.request as req
from http.client import HTTPResponse

url =  'http://www.mobiletrain.org/'
response:HTTPResponse = req.urlopen(url=url)

#验证下载请求是否成功


if response.code == 200:
    print('请求成功')
    print(response.geturl())
    print(response.headers)
    print(response.headers.get('Content-Type'))
    data = response.readlines()
    encodeing = 'utf-8'
    lines = []
    for line in data:
        content_charset = re.findall(br'charset="(.+)"',line)
        if content_charset:
            encodeing = content_charset[0].decode(encoding='utf-8')
            break
    print('查找的编码为%s'%encodeing)
    bytes = b''.join(data)
    print(bytes.decode('utf-8'))