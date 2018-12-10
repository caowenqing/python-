# 利用urllib读取JSON，然后将JSON解析为Python对象：

# -*- coding: utf-8 -*-
from urllib import request

import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context
def fetch_data(url):
    with request.urlopen(url) as f:
        urldata = f.read().decode('utf-8')
    # 将一个json的对象反序列化为Python object?
    return json.loads(urldata)

# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
