# #Rivest Cipher Version 4
# #RC2 64 bit Block Stream  Cipher with size variable 

#from random import random
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto import Random
import base64

# key = Random.new().read(16)
# iv = Random.new().read(16)
# tempkey = SHA.new(iv+key).digest()
# temphexkey = SHA.new(iv+key).hexdigest()
# Flag = ARC4.new(tempkey)
# ascii = Flag.encrypt('Hello World'.encode('ascii'))
# Decrypt = ARC4.new(tempkey)
# dec =Decrypt.decrypt(b'}\x91\x86\xeb\x8fw\xec\xb4\xd4Z\xcf')
# print(Flag)
# print(dec)
# print(tempkey)
# print(temphexkey)
# print(ascii)


#ARC 4 Version 2 

def Encrypt(msg):
    key = Random.new().read(16)
    iv = Random.new().read(16)
    tempkey = SHA.new(iv+key).digest()
    c = ARC4.new(tempkey)
    data = [tempkey,base64.b64encode(c.encrypt(msg.encode('ascii')))]
    return data


def Decrypt(tempkey,Encrypted_message):
    d = ARC4.new(tempkey)
    return d.decrypt(base64.b64decode(Encrypted_message)).decode('ascii')


c = Encrypt('Hello World')
d = Decrypt(c[0],c[1])
print(c[0])
print(c[1])
print (d)
