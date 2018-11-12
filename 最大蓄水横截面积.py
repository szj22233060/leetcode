#coding=utf-8
#milo22233060@gmail.com
#2018/11/1 18:34

def water(nums):
    #先找到最大值，一分为二，左右两边可以蓄水
    max = 0
    for i in range(len(nums)):
        if nums[i]>nums[max]:
            max = i
    print(max)

    left_top = 0    #左半部分从0开始遍历，碰到比nums[0]小的值直接就可以蓄水，先把这个柱子的水加上
    water = 0
    for i in range(1,max):
        if nums[i]>nums[left_top]:

            left_top = i    #更新这个最大值
        else:
            water += nums[left_top] - nums[i]
    print(water)

    right_top = len(nums)-1     #同左半部分，要从最后一个元素开始
    for i in range(len(nums)-1,max,-1):
        print(i)
        if nums[i]>nums[right_top]:
            right_top = i
        else:
            water += nums[right_top] - nums[i]
    print('最大蓄水横截面积',water)
    return water

water([2,1,1,3,2,1,2,4,2,1])

for i in range(10):
    print(i)











