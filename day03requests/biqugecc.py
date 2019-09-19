import requests
from lxml import etree



def download(url):
    resp = requests.get(url)

    if resp.status_code == 200:
        root = etree.HTML(resp.text)
        contents = root.xpath('//div[@class="box_con"]/div[@id="content"]//text()')
        title = root.xpath('//div[@class="con_top"]/a[last()]/text()')[0]
        unite = root.xpath('//div[@class="content_read"]/div[@class="box_con"]/div[@class="bookname"]/h1/text()')[0]
        BASE_URL = url[:-13]
        page = root.xpath('//div[@class="content_read"]/div[2]/div[@class="bottem2"]/a[@id="A3"]/@href')[0]
        next_page_url = BASE_URL+page

        print(unite)
        txt = ''
        for content in contents:
            txt += content.strip()+'\n'
        txt = unite +'\n'+txt
        bytes = txt.encode()
        with open('../day02xpath/txt/%s.txt'%title,'ab') as f:
            f.write(bytes)
        download(next_page_url)



if __name__ == '__main__':
    url = 'https://www.biquge.cc/html/9/9378/18114760.html'
    download(url)



