#coding:utf-8
#milo22233060@gmail.com
#2018/11/19 20:40

'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
'''

import copy

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a = copy.copy(nums1)
        b = copy.copy(nums2)
        # 两个排序数组先排序
        result = []
        for i in range(len(nums1)+len(nums2)):
            if len(nums1) != 0 and len(nums2) != 0:
                if nums1[0] <= nums2[0]:
                    result.append(nums1[0])
                    nums1.pop(0)
                else:
                    result.append(nums2[0])
                    nums2.pop(0)
            else:
                if len(nums1) == 0:
                    result.extend(nums2)
                    break
                else:
                    result.extend(nums1)
                    break
        print(result)
        print(a,b)
        target = 0
        if (len(a)+len(b)) % 2 == 0:
            target = int((len(a)+len(b)) / 2)
            re = (result[target] + result[target-1])/2
        else:
            target = (len(a)+len(b)) // 2
            re = result[target]
        print(re)
        return re

a = Solution()
a.findMedianSortedArrays([1],[6])



print(4/2,4//2,3/2,3//2)




