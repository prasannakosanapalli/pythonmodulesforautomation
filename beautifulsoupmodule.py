import bs4

a=bs4.BeautifulSoup(textfile)
b=a.select("#author")
print(b)
print(b[0])
print(b[1])
b[2].get_text()
a.string()
a.text()
a.get_text()
c=a.find_all('p')
a.title()
a.title.name()
a.title.string()
a.title.text()
a.p()
d=a.find_all('a')
b.get('href')
nav.find_all()
b.find_all('tr')