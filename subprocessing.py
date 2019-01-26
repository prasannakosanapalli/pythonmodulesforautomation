# -*- coding: utf-8 -*-

import subprocess

a=subprocess.run(["cmd","dir"])
b=subprocess.call()
c=subprocess.Popen()
a.poll()
b.wait()
c.kill()
c.terminate()
subprocess.getoutput()
subprocess.getstatusoutput()
subprocess.check_output()
