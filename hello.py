import string

$ cat hello.py 
print('Hello, world!')

$ pyarmor obfuscate hello.py
...

$ cat dist/hello.py
from pytransform import pyarmor_runtime
pyarmor_runtime()
__pyarmor__(__name__, __file__, b'\x50\x59\x41\x52\x4d\x4f\x52\x00\x00\x03\x08\x00\x55\x0d\x0d\
x0a\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x40\x00\x00\x00\xd5\x00\x00\x00\x00\x00\x00
\x18\xf4\x63\x79\xf6\xaa\xd7\xbd\xc8\x85\x25\x4e\x4f\xa6\x80\x72\x9f\x00\x00\x00\x00\x00\x00\x0
0\x00\xec\x50\x8c\x64\x26\x42\xd6\x01\x10\x54\xca\x9c\xb6\x30\x82\x05\xb8\x63\x3f\xb0\x96\xb1\x
97\x0b\xc1\x49\xc9\x47\x86\x55\x61\x93\x75\xa2\xc2\x8c\xb7\x13\x87\xff\x31\x46\xa5\x29\x41\x9d\
xdf\x32\xed\x7a\xb9\xa0\xe1\x9a\x50\x4a\x65\x25\xdb\xbe\x1b\xb6\xcd\xd4\xe7\xc2\x97\x35\xd3\x3e
\xd3\xd0\x74\xb8\xd5\xab\x48\xd3\x05\x29\x5e\x31\xcf\x3f\xd3\x51\x78\x13\xbc\xb3\x3e\x63\x62\xc
a\x05\xfb\xac\xed\xfa\xc1\xe3\xb8\xa2\xaa\xfb\xaa\xbb\xb5\x92\x19\x73\xf0\x78\xe4\x9f\xb0\x1c\x
7a\x1c\x0c\x6a\xa7\x8b\x19\x38\x37\x7f\x16\xe8\x61\x41\x68\xef\x6a\x96\x3f\x68\x2b\xb7\xec\x60\
x39\x51\xa3\xfc\xbd\x65\xdb\xb8\xff\x39\xfe\xc0\x3d\x16\x51\x7f\xc9\x7f\x8b\xbd\x88\x80\x92\xfe
\xe1\x23\x61\xd0\xf1\xd3\xf8\xfa\xce\x86\x92\x6d\x4d\xd7\x69\x50\x8b\xf1\x09\x31\xcc\x19\x15\xe
f\x37\x12\xd4\xbd\x3d\x0d\x6e\xbb\x28\x3e\xac\xbb\xc4\xdb\x98\xb5\x85\xa6\x19\x11\x74\xe9\xab\x
df', 1)

$ python dist/hello.py
Hello, world!

print('Hey')

from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print(password)
