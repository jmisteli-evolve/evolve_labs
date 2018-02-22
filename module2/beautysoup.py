import requests, bs4
res = requests.get('http://eff.org/')

soup = bs4.BeautifulSoup(res.text, 'html.parser')
type(soup)
print(type(soup))

h3 = soup.select('h2')
print(type(h3[0]))