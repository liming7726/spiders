import re
from urllib.request import Request, urlopen, urlretrieve, ProxyHandler, HTTPHandler
from urllib.request import build_opener
from urllib.parse import urlencode
import json


def add_index():
    url = 'http://118.178.180.116:9200/gs_lm'
    params = {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        }
    }
    req = Request(url,json.dumps(params).encode('utf-8'), headers={
        'Content-Type': 'application/json'
    }, method='PUT')

    resp = urlopen(req)
    if resp.code == 200:
        print('创建index成功!!')



def download(url):
    opener = build_opener(HTTPHandler(), ProxyHandler(proxies={'http': ''}))
    req = Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    })
    resp = opener.open(req)
    if resp.code == 200:
        bytes = resp.read()
        datas = bytes.decode('utf-8')
        if datas:
            parse(datas)


def parse(datas):
    title = re.findall('<b>(.*?)</b>', datas)
    if title:
        author = re.findall('<p class="source"><a .*?>(.*?)</a>.*?<a .*?>(.*?)</a>.*?</p>', datas)
        content = re.findall('<div class="contson" .*?>(.*?)</div>', datas, re.DOTALL)
        gs = zip(tuple(title), author, tuple(content))
        for i in gs:
            data = {
                '标题：':i[0],
                '作者：':i[1],
                '内容：':i[2]
            }
            print(data)
            print('1')
            url = 'http://118.178.180.116:9200/gs_lm/text'
            req = Request(url, json.dumps(data).encode('utf-8'), headers={
                'Content-Type': 'application/json'
            })
            resp = urlopen(req)
            if resp.code == 200:
                print('1111111')
                print('古诗%s添加成功'%(i[0]))
            print('到这里来了')
        # 提取下一页
        next_url = re.findall('<a id="amore" .*?href="(.*?)"', datas)
        print(next_url)
        if next_url:
            next_url = 'https://www.gushiwen.org' + next_url[0]
            download(next_url)


if __name__ == '__main__':
    url = 'https://www.gushiwen.org/'
    # add_index()
    download(url)
