import os
import time

os.getcwd()
os.chdir('C:\\Users\\Prasanna\\Desktop\\python practice\\automation tasks')
os.getcwd()
os.listdir()
#os.mkdir('pythonfordevops')
#os.listdir()
#os.makedirs('C:\\Users\\Prasanna\\Desktop\\python practice\\')
a=os.path.abspath(r'path.py')
b='C:\\Users\\Prasanna\\Desktop\\python practice'
c='path.py'
os.path.basename('textfile.txt')
os.path.dirname(a)
os.path.exists('C:\\Users\\Prasanna\\Desktop\\python practice')
os.path.isfile(c)
os.path.isdir(b)
os.path.isabs(c)
d=os.path.getmtime('textfile.txt')
time.ctime(d)
os.path.getsize('textfile.txt')
