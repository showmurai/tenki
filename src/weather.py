# -*- coding:utf-8 -*-

import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Tokyo,jp', )

print r.status_code
print r.headers['content-type']
print r.json()
