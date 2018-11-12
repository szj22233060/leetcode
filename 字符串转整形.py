# coding: utf-8
# @Time   : 2018/9/26 15:12
# @Author : Milo
# @Email  : 1612562704@qq.com
'''
实现 atoi，将字符串转为整数。
该函数首先根据需要丢弃任意多的空格字符，直到找到第一个非空格字符为止。如果第一个非空字符是正号或负号，
选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，
则直接将其与之后连续的数字字符组合起来，形成整数。

字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。

当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。

若函数不能执行有效的转换，返回 0。
'''


import re
class Solution:
    def myAtoi(self, str):
        #去除首尾空格
        str = str.strip()
        #正则，匹配开头+-号和数字
        result = re.compile(r'\+?-?\d+').match(str)
        #匹配结果为空则返回0
        if result == None:
            return 0
        num = result.group(0)
        if num[0] == '+' and num[1] == '-':
            return 0
        print(num)
        num = int(num)
        print(num)
        #判断是否越界
        if num > 2**31-1:
            return 2**31-1
        elif num < -2**31:
            return -2**31
        else:
            return num

res = Solution()
aa = "+-42"
print(res.myAtoi(aa))












