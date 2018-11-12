# coding: utf-8
# @Time   : 2018/10/4 9:29
# @Author : Milo
# @Email  : 1612562704@qq.com

'''

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

说明：

1.num1 和 num2 的长度小于110。
2.num1 和 num2 只包含数字 0-9。
3.num1 和 num2 均不以零开头，除非是数字 0 本身。
4.不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
'''

class Solution:
    def multiply(self, num1, num2):
        res = [0 for i in range(len(num1+num2))]
        num1 = num1[::-1]
        num2 = num2[::-1]
        print(res)
        for i in range(len(num2)):
            for j in range(len(num1)):
                res[i+j] += int(num2[i]) * int(num1[j])
        print(res)
        result = []
        for i in range(len(res)):
            digit = res[i] % 10
            carry = res[i] // 10
            if i < len(res) - 1:
                res[i+1] += carry
            result.append(str(digit))
        result.reverse()
        while result[0] == "0" and len(result)>1:
            del result[0]
        print(result)
        return "".join(result)

a = Solution()
print(a.multiply("0","123400"))
print(999*123400)


