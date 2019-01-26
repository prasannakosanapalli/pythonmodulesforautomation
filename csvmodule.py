# -*- coding: utf-8 -*-

import csv
b= file path
a= csv.reader(b)


for line in a:
    print(line)
    print(line[0])
    print(line[1])
d=[]
a= csv.DictWriter(b,fielname=d,delimuter='-')
a.writerow()
a.writeheader(d)

a=csv.wrtiter(b)
a.writeheader()
a.writerow() 
 