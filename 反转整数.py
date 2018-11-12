#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/16 20:42

class Solution:
    def reverse(self, x):
        if not self.judge(x):
             return 0

        num = str(x)
        if num[0] == '-':
            result = int('-'+num[1:].strip()[::-1])
            if self.judge(result):
                return result
            else:
                return 0
        else:
            result = int(num.strip()[::-1])
            if self.judge(result):
                return result
            else:
                return 0

    def judge(self,num):
        if num<=2**31-1 and num>=-2**31:
            return 1
        else:
            return 0

a = Solution()
print(a.reverse(1534236469))













