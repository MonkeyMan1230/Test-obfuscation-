import base64
import string

f = open('Other-Test.py')
encoded = base64.b64encode(f.read())

mycode = "print 'Hello World!'"
secret = base64.b64encode(mycode)
secret
'cHJpbnQgJ2hlbGxvIFdvcmxkICEn'
mydecode = base64.b64decode(secret)
eval(compile(mydecode,'<string>','exec'))
Hello World!

print('Hey')

from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print password
