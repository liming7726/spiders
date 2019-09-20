import json

import requests







BASE_URL = 'http://118.178.180.116:9200'

def add_index(index_name):
    url = f'{BASE_URL}/{index_name}'
    params = {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        }
    }

    try:
        resp = requests.put(url,json.dumps(params))
        ret = resp.json()
        print(ret)
        return ret['acknowledged']
    except:
        return False


def delete_index(index_name):
    url = f'{BASE_URL}/{index_name}'
    resp = requests.delete(url)
    ret = resp.json()
    return ret['acknowledged']


def add_doc(index_name,typename,**kwargs):
    if kwargs.get('id'):
        url = f'{BASE_URL}/{index_name}/{typename}/{kwargs["id"]}'
        kwargs.pop('id')
    else:
        url = f'{BASE_URL}/{index_name}/{typename}'
    resp = requests.post(url,json=kwargs)
    ret = resp.json()
    return ret['created']

def update_doc(index_name,typename,id,**kwargs):
    url = f'{BASE_URL}/{index_name}/{typename}/{id}'
    resp = requests.put(url,json=kwargs)
    ret = resp.json()
    return ret

def delete_doc(index_name,typename,id):
    url = f'{BASE_URL}/{index_name}/{typename}/{id}'
    resp = requests.delete(url)
    ret = resp.json()
    return ret

def query(index_name,kw=None):
    url = f'{BASE_URL}/{index_name}'
    resp = requests.get(url,params={
        "q":kw if kw else ''
    })
    result = resp.json()
    hits =  result['hits']['hits']
    datas = []
    for source in hits:
        data = source['_source']
        data['id'] = source['_id']
        datas.append(data)
    return datas

if __name__ == '__main__':
    delete_index('proxy_lm')




