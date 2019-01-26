import re


with open('textfile.txt','r', encoding=None) as f:
    reading= f.read()
    a= re.compile(r'abc')
    b=a.findall(reading)
    for match in b:
        print(match,'matching')
        
    