import json
from urllib.request import urlopen, Request

from request import get

from lxml import etree


BASE_URL = 'http://www.tbqq.net/'

def download(url):
    resp = get(url)
    if resp.code == 200:
        html = resp.read().decode('gbk')
        parse(html)


def parse(html):
    root = etree.HTML(html)
    li_elemnts = root.xpath('//li[starts-with(@class,"deanactions")]')
    for li_elemnt in li_elemnts:
        cover_url = li_elemnt.xpath('./div[1]//img/@src')[0]
        img_url = BASE_URL+cover_url
        name = li_elemnt.xpath('.//div[@class="deanmadouname"]//text()')[0]
        zhiye =  li_elemnt.xpath('.//div[@class="deanmadouzhiye"]//text()')[-1]
        city =  li_elemnt.xpath('.//div[@class="deanmadouinfos"]/div[5]/text()')[0].strip()
        city = city[4:]
        height_dtat = li_elemnt.xpath('.//div[@class="deanmadouinfos"]/div[2]/div[1]//text()')
        height = height_dtat[0]+height_dtat[1]
        weight = height_dtat[2]+height_dtat[3]
        hot = li_elemnt.xpath('.//div[@class="deanmadouinfos"]/div[2]/div[2]//text()')[-1]
        data ={
            "img_url":img_url,
            "name":name,
            "zhiye":zhiye,
            "city":city,
            "height":height,
            "weight":weight,
            "hot":hot
        }
        # print(img_url,name,zhiye,city,height,weight,hot)
        saveessearch(data)
        save(img_url,name)
    page = root.xpath('//a[@class="nxt"]/@href')[0]
    next_page = BASE_URL + page
    download(next_page)


def save(img_url,name):
    #保存数据
    #保存图片，名称为模特名
    img = urlopen(img_url)
    if img.code == 200:
        bytes = img.read()
        with open('sucai/%s.jpg' % name, 'wb') as f:
            f.write(bytes)

def saveessearch(data:dict):
    url = 'http://118.178.180.116:9200/gs_lm/text'
    req = Request(url,json.dumps(data).encode('utf-8'),{
        'Content-Type': 'application/json'
    })
    resp = urlopen(req)


if __name__ == '__main__':
    url = 'http://www.tbqq.net/'
    download(url)
