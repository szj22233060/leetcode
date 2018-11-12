#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/16 9:36



class Solution:
    def isPalindrome(self, x):
        x = str(x)
        if x[0] == '-':
            return False
        if x[0] == '+':
            x = x[1:]
        i = 0
        while i <= len(x)//2:
            if x[i] != x[-i-1]:
                return False
            i += 1
        return True




a = Solution()
print(a.isPalindrome(123211))













