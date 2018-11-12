#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/12 8:14

'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

'''

class Solution:
    def spiralOrder(self, matrix):
        #递归的方法，case表明是哪一种情况，0对应向右， 1对应向下，2 对应向左，3对应向上
        # ri, ci 表示我们当前遍历的点的位置坐标。
        # row, col, 用来代表这一次运动的步数。
        def circle(case,ri,ci,row,col):
            if row == 0 or col == 0:
                return

            #向右
            if case == 0:
                #结束坐标是开始列加col
                end = ci+col
                #向右走结束后行数-1
                row -= 1
                for i in range(ci,end):
                    result.append(matrix[ri][i])
                ri += 1
                ci = end-1
                case = (case+1)%4
                circle(case,ri,ci,row,col)
            #向下
            elif case == 1:
                end = ri+row
                col -= 1
                for i in range(ri,end):
                    result.append(matrix[i][ci])
                ci -= 1
                ri = end-1
                case = (case+1)%4
                circle(case,ri,ci,row,col)
            #向左
            elif case == 2:
                end = ci-col
                row -= 1
                for i in range(ci,end,-1):
                    result.append(matrix[ri][i])
                ri -= 1
                ci = end+1
                case = (case+1)%4
                circle(case,ri,ci,row,col)
            #向右
            elif case == 3:
                end = ri-row
                col -= 1
                for i in range(ri,end,-1):
                    result.append(matrix[i][ci])
                ci += 1
                ri = end+1
                case = (case+1)%4
                circle(case,ri,ci,row,col)

        row = len(matrix)
        col = len(matrix[0])
        result = []
        if row == 0:
            return []
        circle(0,0,0,row,col)
        return result
        # print(result)
a = Solution()
a.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])












