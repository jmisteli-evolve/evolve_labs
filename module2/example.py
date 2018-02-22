import requests, bs4

res = requests.get("http://example.com")
try:
	res.raise_for_status()
except:
	print("this is not working lads")
soup = bs4.BeautifulSoup(res.text, 'html.parser')

p = soup.select('p')
print(p[0].get_text())
content = open("example.txt", "w")
for x in range(0, len(p)):
	content.write(p[x].get_text())

content.close()