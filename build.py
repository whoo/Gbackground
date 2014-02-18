#!/usr/bin/env python


import zipfile
import os,stat

#


with zipfile.ZipFile('Gbackground.zip', 'w', zipfile.ZIP_DEFLATED) as myzip:
	myzip.write('__main__.py')
	myzip.close()

a=open("Gbackground.py","wb")
a.write(b"#!/usr/bin/env python\n")
a.write(open('Gbackground.zip','rb').read())
os.chmod('Gbackground.py',stat.S_IRWXU|stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH|stat.S_IXOTH)
print(stat.S_IRWXU|stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH|stat.S_IXOTH)
os.unlink('Gbackground.zip')
