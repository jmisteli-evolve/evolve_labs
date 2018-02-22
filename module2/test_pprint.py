import pprint
import requests

r = requests.post('http://httpbin.org/post', data={'key':'value'})

pprint.pprint(r.json())
