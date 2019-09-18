from urllib.request import urlopen,Request
from urllib.parse import urlencode,quote,unquote


url = 'https://wwww.baidu.com/s?wd='+quote('香港')
req = Request(url,headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
})

resp = urlopen(req)
bytes = resp.read()
print(bytes.decode('utf-8'))