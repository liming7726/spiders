from urllib.request import urlopen

from lxml import etree

from request import get





def download(url):
    resp = get(url)
    if resp.code == 200:
        bytes = resp.read()
        html = bytes.decode('utf-8')
        parse(html)


def parse(html):
    root = etree.HTML(html)
    img_elements = root.xpath('//div[@id="container"]/div/div/a/img')
    for element in img_elements:
        url = element.get('src2').replace('_s','')
        name = element.get('alt')
        save(url,name)

def save(url,name=None,flage=False):
    img = urlopen(url)
    if img.code == 200:
        bytes = img.read()
        with open('sucai/%s.jpg' % name, 'wb') as f:
            f.write(bytes)



if __name__ == '__main__':
    i = 1
    while True:
        if not i == 1:
            url_str = '_'+str(i)
            url = 'http://sc.chinaz.com/tupian/hunsha%s.html'%url_str
        else:
            url = 'http://sc.chinaz.com/tupian/hunsha.html'
        print(url)
        download(url)
        i += 1


