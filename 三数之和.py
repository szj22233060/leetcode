# coding: utf-8
# @Time   : 2018/10/1 10:01
# @Author : Milo
# @Email  : 1612562704@qq.com

'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
#排列组合
from itertools import product,combinations
import operator
class Solution:
    def threeSum(self, nums):
        #排列
        # print(list(product(nums,repeat=2)))
        #组合
        result_list = list(combinations(nums, 3))
        result = []
        for i in result_list:
            if i[0]+i[1]+i[2] == 0:
                i = list(i)
                i.sort()
                result.append(list(i))
        combina = combinations(result,2)
        for i in combina:
            if operator.eq(i[0],i[1]):
                result.remove(i[0])
        print(result)
        return result
    #最接近target值的三数之和
    def minThreeSum(self,nums,target):
        result_list = list(combinations (nums, 3))
        result = []
        for i in range(len(result_list)):
            result.append(abs(result_list[i][0]+result_list[i][1]+result_list[i][2]-target))
        mini = result.index(min(result))
        print(list(result_list[mini]))
        num = 0
        for i in result_list[mini]:
            num += i
        print(num)
        return num
nums = [-1, 0, 1, 2, -1, -4]
a = Solution()
a.minThreeSum([-1,2,1,-4],1)
a.threeSum(nums)







