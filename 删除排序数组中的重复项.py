# coding: utf-8
# @Time   : 2018/10/3 16:47
# @Author : Milo
# @Email  : 1612562704@qq.com

'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
'''

class Solution:
    def removeDuplicates(self, nums):
        k = 0
        while k < len(nums) - 1:
            if nums[k] == nums[k+1]:
                nums.remove(nums[k])
            else:
                k += 1
        print(nums)
        return len(nums)
a = Solution()
a.removeDuplicates([1,1,1,1,2,2,3,3,4])

