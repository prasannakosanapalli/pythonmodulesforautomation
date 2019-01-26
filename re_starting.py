# -*- coding: utf-8 -*-
import re

message = 'Call me at 415-555-1011 tomorrow and today 415-555-9999 is towards my office.'
"""
a= re.compile(r'\d\d\d-\d{3}-\d{4}')
b=a.search(message)
print(b.groups())

a= re.compile(r'(\d\d\d)-(\d{3}-\d{4})')
b=a.search(message)
print(b.group(1))
print(b.group(2))
#print(b.group(3))
print(b.group(0))
print(b.groups())

c,d = b.groups()
print(c)
print(d)

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.groups())
print(mo.group(1))

searchingpattern =re.compile(r'my|me')
content =searchingpattern.search(message)
content.group()
"""
"""
a= re.compile(r'to(day|morrow|wards)')
b=a.search(message)
b.group()

"""
batRegex = re.compile(r'Bat(man)+')
mo1 = batRegex.search('The Adventures of  is there any Batman in the Batmanmanman world asia Batman')
mo1.group()

