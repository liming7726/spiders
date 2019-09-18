import re
from urllib.request import urlopen,Request
from urllib.parse import urlencode,unquote,quote




def get_haha():
    url = 'http://www.haha56.net/xiaohua/zuixin/'
    resp = urlopen(url)
    if resp.code == 200:
        print('请求成功！！')
        bytes = resp.read()
        data = bytes.decode('GBK')
        contnet_type = re.findall(br'charset=(.+)',bytes)
        with open('haha1.html','wb') as f:
            f.write(bytes)
        print(data,contnet_type)



if __name__ == '__main__':
    get_haha()