import shutil, os
import send2trash
shutil.copy(src,dst)

shutil.copytree(src,dst)
shutil.move(src,dst)
shutil.rmtree(src,dst)

send2trash.send2trash(path)

