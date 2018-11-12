# coding: utf-8
# @Time   : 2018/10/2 23:15
# @Author : Milo
# @Email  : 1612562704@qq.com

'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
'''

#把字符元素放进栈里，先进后出
class Solution:
    def isValid(self, s):
        s_dict = {')': '(', ']': '[', '}': '{'}
        #L不能为空，不然判断成功后无法出栈
        L = [None]
        for i in s:
            if i in s_dict and s_dict[i] == L[-1]:
                L.pop()
            else:
                L.append(i)
        print(L)
        print(len(L) == 1)
        return len(L) == 1
a = Solution()
a.isValid("()[]{}")



