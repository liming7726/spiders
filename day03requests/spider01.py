import requests
from lxml import etree

class BookItem(dict):
    pass

class ChapterItem(dict):
    pass

def download(url,callback=None,**kwargs):
    resp = requests.get(url=url,timeout=10)
    resp.encoding = 'gbk'
    if resp.status_code == 200:
        html = resp.text
        if callback:
            callback(html,**kwargs)
        else:
            parse(html)
    else:
        print('请求失败')

def parse(html):
    root = etree.HTML(html)
    nav_list = root.xpath('//ul[@class="channel-nav-list"]/li/a')[:-1]
    for nav in nav_list:
        print(nav.get('href'),nav.text)
        download(nav.get('href'),parse_book)





def parse_book(html):
    root = etree.HTML(html)
    seewell_list = root.xpath('//ul[@class="seeWell cf"]/li')
    for seewell in seewell_list:
        item = BookItem()
        item["cover_url"],item["name"] = seewell.xpath('./a/img/@src | ./a/img/@alt')
        item["author"] =seewell.xpath('./span/a[2]/text()')[0]
        item["info"] = seewell.xpath('./span/em/text()')[0]
        item["info_url"] = seewell.xpath('./span/a[last()]/@href')[0]
        if item["cover_url"].find('nocover.jpg') > 0 :
            cover_url = ''
        print(item)

        download(item["info_url"],parse_info,bookname=item["name"])


def parse_info(html,bookname):
    root = etree.HTML(html)
    read_url = root.xpath('//div[@class="b-oper"]/a[1]/@href')[0]
    download(read_url,parse_chap,bookname=bookname)


def parse_chap(html,bookname):
    root = etree.HTML(html)
    chap_lis = root.xpath('//div[@class="clearfix dirconone"]/li')
    for chap in chap_lis:
        item = ChapterItem()
        item["chap_url"],item["title"] = chap.xpath('./a/@href | ./a/text()')
        item["name"] = bookname
        itempeline(item)




def itempeline(item):
    if isinstance(item,BookItem):
        print('--书的信息--')
        print(item)
    else:
        print('--章节--')
        # print(item)
        # print(item.get('chap_url'))
        download(item.get('chap_url'),txt,item=item)

def txt(html,item):
    root = etree.HTML(html)
    txts = root.xpath('//div[@class="mainContenr"]/text()')
    content = ''
    for txt in txts:
        content +=  txt.strip() + '\n'
    chap = item['title'] + content
    content = chap.encode()
    with open('../day02xpath/txt/%s.txt'%item["name"],'ab') as f:
        f.write(content)
        print('%s保存成功'%item['title'])


if __name__ == '__main__':
    url = 'http://www.quanshuwang.com/'
    download(url)