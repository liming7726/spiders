import json

import requests
from bs4 import BeautifulSoup, Tag
import lxml
from request import ua


def download(url, data=None, callback=None, **kwargs):
    headers = {
        'User-Agent': ua.get()
    }

    if not data:
        resp = requests.get(url, headers=headers)
    else:
        # headers['Accept'] = 'application/json'
        resp = requests.post(url, data=data, headers=headers)

    if resp.status_code == 200:
        content_type = resp.headers['Content-Type']
        if content_type.startswith('text/'):
            html = resp.content
            resp_text = html[len('\xef\xbb\xbf'):]
            html = json.loads(resp_text)
            html = html['postlist']
            parse(html)
        else:
            resp_json = resp.json()
            print(resp_json)

        if callback:
            callback(resp.text, **kwargs)
        else:
            parse(resp.text)


def parse(html, **kwargs):
    bs = BeautifulSoup(html, 'lxml')
    # tag : Tag = bs.find('title').text
    content_box_list: Tag = bs.find_all('div', class_='content-box')
    for content_box in content_box_list:
        item = {}
        item['name'] = content_box.find('a').attrs.get('title')
        item['url'] = content_box.a.img.attrs.get('src')
        item['info'] = content_box.a['href']

        itempeline(item)




def itempeline(item):
    resp = requests.get(item['url'])
    with open('image/%s.jpg'%(item['name']),'wb') as f:
        f.write(resp.content)


if __name__ == '__main__':
    # download('http://www.meinv.hk/')
    moreurl = 'http://www.meinv.hk/wp-admin/admin-ajax.php'
    # 加载更多
    for page in range(1, 39):
        """
            total: 39
            action: fa_load_postlist
            paged: 2
            home: true
            wowDelay: 0.3s
        """
        data = {
            "total": 39,
            "action": 'fa_load_postlist',
            "paged": page,
            "home": 'true',
            "wowDelay": '0.3s',
        }
        print(data )
        download(moreurl,data=data)