import requests
from bs4 import BeautifulSoup, Tag


def download(url,callback=None):
    resp = requests.get(url)
    if resp.status_code == 200:
        resp.encoding = 'GBK'
        html = resp.text
        if callback:
            callback(html)
        else:
            parse(html)

def parse(html):
    bs = BeautifulSoup(html,'lxml')
    tags = bs.select('.list_title>ul>li')
    BASE_URL = 'http://www.jokeji.cn'
    next_page = bs.select('.next_page>a')
    next_page = next_page[-1].get('href')
    print(next_page.split('_')[1].split('.')[0])
    for tag in tags:
        print(tag.b.a['href'],tag.b.a.text)
        download(BASE_URL+tag.b.a['href'],parse_info)



def parse_info(html):
    bs = BeautifulSoup(html,'lxml')
    title:Tag = bs.select_one('h1 a')
    title = title.next_sibling.next_sibling.next_sibling
    p_tags = bs.select('#text110>p')
    content = [p.text for p in p_tags]
    print(content)

def main():
    for i in range(1,632):
        download('http://www.jokeji.cn/list_%s.htm'%i)
if __name__ == '__main__':
    # url = 'http://www.jokeji.cn/list.htm'
    # download(url)
    main()
