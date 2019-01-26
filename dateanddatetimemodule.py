# -*- coding: utf-8 -*-

import time
import datetime

a=time.time()
print(a)
print(round(a,2))
print(round(a))
b=datetime.datetime.now()
print(b)
c=datetime.datetime(2019,1,24,16,30,0)
print(c)
"""c.date()
c.time()
c.year()
c.month()
c.day()"""

d=datetime.timedelta(days=11)
print(d.min)
datetime.datetime.today()