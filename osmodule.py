import os 

a=r"D:\DevOps Document"
d=r''
for root,subdirs,files in os.walk(a):
    print(root,"root")
    print(subdirs,"directories")
    print(files,'files')
    for file in files:
        b=os.path.join(root,file)
        shutil.move(c,b)
        print(os.listdir(c))
        