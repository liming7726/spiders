from urllib.request import urlopen,Request
from urllib.parse import urlencode


def save(page,bytes):
    with open('douban%s.json'%page,'wb') as f:
        f.write(bytes)


def download(type,page):
    url ='https://movie.douban.com/j/new_search_subjects?'

    data = {
        'sort':'U',
        'range':'0,10',
        'tags':'',
        'start': page,
        'genres':type
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    req = Request(url+urlencode(data),method='GET',headers=headers)

    resp = urlopen(req)
    if resp.code == 200:
        print('请求成功！！')
        bytes = resp.read()
        save(page,bytes)


if __name__ == '__main__':
    for page in range(1,6):
        print('开始下载第%s页'%page)
        download('动作',page)
        print('下载完成')