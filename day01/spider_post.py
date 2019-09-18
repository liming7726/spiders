import json
from urllib.request import Request,urlopen
from urllib.parse import urlencode



url = 'https://fanyi.baidu.com/sug'

data = {
    'kw':'app',
}

headers = {
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}
data = urlencode(data).encode()
req = Request(url=url,data=data,headers=headers)

resp = urlopen(req)
byte = resp.read()
data =byte.decode()
data = json.loads(data)
print(data)