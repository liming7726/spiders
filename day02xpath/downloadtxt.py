import re
import time
from urllib.request import urlopen,urlretrieve
from lxml import etree

from request import get

def download(url):
    resp = get(url)
    if resp.code == 200:
        # encode_type = resp.headers.get('Content-Type')
        # charset = re.findall(br'charset=(.+)',resp.read())
        # print(charset)
        html =  resp.read()
        # print(html)
        parse(html,url)

def parse(html,url):
    root = etree.HTML(html)
    name = root.xpath('/html/head/title/text()')[0].split("_")[0]
    title = root.xpath('//div[@class="mlfy_main"]/div/h3/text()')[0]
    contents = root.xpath('//div[@class="mlfy_main"]/div/div[@class="read-content"]/text()')
    # time.sleep(2)
    print(url[31:39])
    if url[31:39] == '17974163':
        next_page = '/45/45079/17974165.html'
    elif url[31:39] == '17974161':
        next_page = '/45/45079/17974163.html'
    elif url[31:39] == '17974177':
        next_page = '/45/45079/17974179.html'
    elif url[31:39] == '17974185':
        next_page = '/45/45079/17974186.html'
    else:
        next_page = root.xpath('//p[@class=" mlfy_page"]/a[last()]/@href')[0]
    BASE_URL = 'http://www.635000.net'
    next_page_url = BASE_URL+next_page
    print(next_page_url)
    content_txt = ''
    for content in contents:
        content_txt = content_txt+content.strip()+'\n'
    with open('txt/%s.txt'%name,'a') as f :
        f.write(title)
        f.write('\n')
        f.write(content_txt)
    time.sleep(1)
    download(next_page_url)

if __name__ == '__main__':
    url = 'http://www.635000.net/45/45079/17974145.html'
    download(url)
    # urlretrieve(url,'txt.html')



