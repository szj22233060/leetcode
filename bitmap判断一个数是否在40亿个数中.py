#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/18 9:00
from bitarray import bitarray
import hashlib
class bitmap:
    def __init__(self,size):
        self.size = size
        self.bitarr = bitarray(size)
        self.bitarr.setall(0)
    def add(self,s):
        for i in s:
            result = int(hashlib.sha1(i).hexdigest(),16) % self.size
            print(result)
            self.bitarr[result] = 1
        print(bitarray)
    def test(self,s):
        result = int(hashlib.sha1(s).hexdigest(), 16) % self.size
        if self.bitarr[result] == 1:
            return 'Got it'
        else:
            return 'Nope'
size = 100
a = bitmap(size)
a.add([1,2,3,4])
a.test(3)












