import requests

url="https://docs.python.org/3/index.html"

a=requests.get(url)
a.encoding = 'ISO-8859-1'
b=a.text()
c=a.headers()
d=a.cookies()
e=a.cookies.get_dict()
f=a.url()
a.status_code == a.code.ok
a.raise_for_status()
a.iter_content()
print(a.text)
