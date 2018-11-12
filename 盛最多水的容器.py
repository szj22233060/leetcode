# coding: utf-8
# @Time   : 2018/10/5 10:48
# @Author : Milo
# @Email  : 1612562704@qq.com

"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
"""
#排列组合
from itertools import product,combinations
from scipy.special import comb,perm

class Solution:
    def maxArea(self, height):
        for i in range(len(height)):
            height[i] = [i+1,height[i]]
        print(height)
        mid_list = list(combinations(height,2))
        print(mid_list)

        area_list = []
        for i in mid_list:
            area = abs(i[0][0]-i[1][0]) * min(i[0][1],i[1][1])
            area_list.append(area)
        return max(area_list)



print(comb(3,2),perm(3,2))

a = Solution()
a.maxArea([1,8,6,2,5,4,8,3,7])


