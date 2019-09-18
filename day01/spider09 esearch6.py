from urllib.request import Request, urlopen

import json

BASE_URL = 'http://xm.imzhangao.com:9200'


def add_index(index_name):
    url = BASE_URL + '/' + index_name
    print(url)
    params = {
        "settings" : {
        "number_of_shards" : 5,
        "number_of_replicas" : 1
        }
    }
    req = Request(url=url,
                  data=json.dumps(params).encode('utf-8'), headers={
            'Content-Type': 'application/json'
        }, method='PUT')

    resp = urlopen(req)
    if resp.code == 200:
        bytes = resp.read()
        resp_json = json.loads(bytes.decode('utf-8'))
        print(resp_json)

def add_city(index,type,id=None):
    url = BASE_URL+'/'+index+'/'+type+'/'
    if id:
        url = BASE_URL+'/'+index+'/'+type+'/'+str(id)

    print(url)
    params = {
        'type':'http',
        'host':'39.135.24.11',
        'port':'8080',
        'city':'北京市',
        'yys':'移动'
    }
    resp = urlopen(Request(url,json.dumps(params).encode('utf-8'),{
        'Content-Type':'application/json'
    }))
    if resp.code == 200:
        bytes = resp.read()
        resp_json = json.loads(bytes.decode('utf-8'))
        print(resp_json)


def delete_city(index,type,id=None):
    url = BASE_URL + '/' + index + '/' + type + '/'
    if id:
        url = BASE_URL + '/' + index + '/' + type + '/' + str(id)

    print(url)
    resp = urlopen(Request(url,headers= {
        'Content-Type': 'application/json'
    },method='DELETE'))
    if resp.code == 200:
        bytes = resp.read()
        resp_json = json.loads(bytes.decode('utf-8'))
        print(resp_json)


if __name__ == '__main__':
    # delete_city('proxy_ips','ips','0')
    add_city('proxy_lm','text','0')
    # add_index('proxy_lm')