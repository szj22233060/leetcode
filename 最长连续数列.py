# coding: utf-8
# @Time   : 2018/10/6 11:29
# @Author : Milo
# @Email  : 1612562704@qq.com

"""
输入一个乱序的连续数列，输出其中最长连续数列长度，要求算法复杂度为 O(n) 。
[3,2,5,1,7,4]
{3:1}
{3:2,2:2}
{3:2,2:2,5:1}
{3:3,2:2,5:1,1:3}
{3:3,2:2,5:1,1:3,7:1}
{3:3,2:3,5:5,1:5,7:1,4:5}
"""
class Solution:
    def solution(self,line):
        a = line.split(',')
        nums = []
        for i in a:
            nums.append(int(i))
        result = {}
        ma = 0
        for i in nums:
            if i in result.keys():
                continue
            left = 0
            right = 0
            left_key = i-1
            right_key = i+1

            if left_key in result.keys():
                left = result[left_key]

            if right_key in result.keys():
                right = result[right_key]

            length = left+right+1
            result[i] = length
            result[i+right] = length
            result[i-left] = length
            ma = max(ma,length)
        print(ma)


a = Solution()
a.solution('2,3,4,1,5,8,9,0,70')


