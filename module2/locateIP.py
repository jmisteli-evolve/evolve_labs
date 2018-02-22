import requests

r = requests.get('http://httpbin.org/ipds')
err = r.raise_for_status()
if err != None:
	print("not happening")
print(r.raise_for_status())

body = r.json()
print(body["origin"])
