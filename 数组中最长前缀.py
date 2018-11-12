# coding: utf-8
# @Time   : 2018/9/28 9:46
# @Author : Milo
# @Email  : 1612562704@qq.com

'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

输入: ["flower","flow","flight"]
输出: "fl"
'''

class Solution:
    def longestCommonPrefix(self, strs):
        #确定共同前缀最小值即循环次数
        min_num = min([len (i) for i in strs])
        s = 0
        #保存结果
        result_strs = ""
        #按照最小值循环
        while s <= min_num-1:
            result = strs[0][s]
            for i in range(len(strs)):
                #如果有共同前缀，并且循环到数组最后一个元素了就添加这个字符
                if strs[i][s] == result and i == len(strs)-1:
                    result_strs += strs[i][s]
            s += 1
        print("最长公共前缀:",result_strs)
        return result_strs

string = ["flower", "flow", "flight"]
a = Solution()
a.longestCommonPrefix(string)



