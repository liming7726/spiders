import requests

from ydm import ydm


session = requests.session()



def get_code():
    code_url = 'https://so.gushiwen.org/RandCode.ashx'
    resp = session.get(code_url)
    with open('yzm.jpg','wb') as f:
        f.write(resp.content)
    code = ydm('yzm.jpg')
    return code


def login():
    url = 'https://so.gushiwen.org/user/login.aspx'
    data = {
        "email":'610039018@qq.com',
        "pwd":'disen8888',
        "code":get_code()
    }
    resp = session.post(url,data)
    print(resp.text)
    with open('gswlogin.html','wb') as f:
        f.write(resp.content)



if __name__ == '__main__':
    login()