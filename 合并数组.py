#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/9 10:46

'''
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
'''
class Solution:
    def merge(self, nums1, m, nums2, n):
        item = [0 for i in range(m+n)]
        print(item)
        i,j,k = 0,0,0

        while i<m and j<n:
            if nums1[i]<nums2[j]:
                item[k] = nums1[i]
                i += 1
            else:
                item[k] = nums2[j]
                j += 1
            k += 1
        print(item)
        if i == m:
            while k < m+n:
                item[k] = nums2[j]
                k += 1
                j += 1
        else:
            while k < m+n:
                item[k] = nums1[i]
                i += 1
                k += 1
        print(item)
        nums1 = item
        print(nums1)


a = Solution()
a.merge([1,2,3,0,0,0],3,[2,5,6],3)





















