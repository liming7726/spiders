import re
from urllib.request import urlopen

import requests

url = 'https://sou.zhaopin.com/?jl=530&kw=python&kt=3'

# resp = urlopen(url)  #http.client.HTTPResponse
# if resp.code == 200:
#     bytes = resp.read()
#     data = bytes.decode('utf-8')
#     content_type = re.findall(br'charset=(.+)',bytes)
#     print(content_type)
#     # print(bytes)
#     # print(resp.read().decode('utf-8'))
#     # print(resp.headers.get('Content-Type'))
#     # body = resp.read()
#     # print(body)
#     with open('zhaopin_python.html',mode='wb') as f:
#         f.write(bytes)

z_p = requests.get(url)
data = z_p.text.encode()
with open('zhaopin_python.html',mode='wb') as f:
    f.write(data)
