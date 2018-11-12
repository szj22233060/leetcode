#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/16 22:22

'''
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

二进制中，如果是2的n次方，为100000，，，1后面n个0，减1之后变成011111.。。n个0变成了1
x与x-1相与，判断结果是不是0就行了
'''

class Solution:
    def isPowerOfTwo(self, n):
        if n & (n-1) == 0:
            return True
        else:
            return False

a = Solution()
print(a.isPowerOfTwo(16))














