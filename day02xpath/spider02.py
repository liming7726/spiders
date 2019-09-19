from http.client import HTTPResponse
from urllib.request import urlopen
from lxml import etree


def parse(html):
    root = etree.HTML(html)
    sons_elements = root.xpath('//div[@class="sons"]')
    for sons_element in sons_elements:
        title = sons_element.xpath('.//p[1]//b/text()')
        author = sons_element.xpath('.//p[2]/a/text()')
        content = sons_element.xpath('.//div[@class="contson"]/text()')

        if not title:
            break
        print(title[0],author[0],author[1],content)


def download(url):
    resp : HTTPResponse = urlopen(url)
    if resp.code ==200:
        bytes = resp.read()
        html = bytes.decode('utf-8')
        parse(html)

if __name__ == '__main__':
    url = 'https://www.gushiwen.org/'
    download(url)