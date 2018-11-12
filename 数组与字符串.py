# coding: utf-8
# @Time   : 2018/9/25 21:20
# @Author : Milo
# @Email  : 1612562704@qq.com

#1.给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000
# 输入: "babad"
# 输出: "bab"
# 注意: "aba"也是一个有效答案。
#c d a b c d e d c b a
#0 1 2 3 4 5 6 7 8 9 10

import copy
class Solution:
    def longestPalindrome(self, s):
        list_s = list(s)
        print("list_s:",list_s)
        #保存结果数组
        result_list = []

        #保存每一个结果，存进result_list
        mid_list = []

        #顺序遍历数组
        for i in range(len(list_s)):
            #回文开始点与上上个相等
            if i-2 >= 0 and list_s[i] == list_s[i-2]:
                #如果相等就先加进数组中后续如果相等会继续添加
                mid_list += [list_s[i-1],list_s[i]]
                #设置两个变量表示开始点
                a = b = i
                #继续遍历数组，如果还是相等就继续添加，直到条件不成立
                while a+1 <= len(list_s)-1 and b-3 >= 0 and list_s[a+1] == list_s[b-3]:
                    mid_list.append(list_s[a+1])
                    a += 1
                    b -= 1
                #中间数组，反转，添加成完整回文串
                mid = copy.copy(mid_list)
                mid_list.reverse()
                mid_list += mid[1:]

                #添加进结果数组进行比较长度，找到最长数组
                result_list.append(mid_list)
            #asdffdsa
            elif i-2 >= 0 and list_s[i] == list_s[i-1]:
                # 如果相等就先加进数组中后续如果相等会继续添加
                mid_list += [list_s[i]]
                # 设置两个变量表示开始点
                a = b = i
                # 继续遍历数组，如果还是相等就继续添加，直到条件不成立
                while a + 1 <= len (list_s) - 1 and b - 2 >= 0 and list_s[a + 1] == list_s[b - 2]:
                    mid_list.append (list_s[a + 1])
                    a += 1
                    b -= 1
                # 中间数组，反转，添加成完整回文串
                mid = copy.copy (mid_list)
                mid_list.reverse ()
                mid_list += mid
                # 添加进结果数组进行比较长度，找到最长数组
                result_list.append (mid_list)
            mid_list = []
        print("result_list:",result_list)
        length = [len(i) for i in result_list]

        print("最长回文串：",result_list[length.index(max(length))])
        result = result_list[length.index(max(length))]
        result_string = ""
        for i in result:
            result_string += i
        return result_string

a = Solution()
print(a.longestPalindrome("abcdcbatyuytuji"))
