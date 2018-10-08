import base64,os
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key): 
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()


    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

def enc(file,obj):
    f=open(file,"rb")
    pt=f.read()
    f.close()
    ct=obj.encrypt(pt)
    f=open(file,"wb")
    f.write(ct)
    f.close()

def dec(thefile,obj):
    f=open(thefile,"rb")
    pt=f.read()
    f.close()
    ct=obj.decrypt(pt)
    f=open(thefile,"wb")
    f.write(ct)
    f.close()
