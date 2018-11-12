#coding=utf-8
#author:milo
#email:milo22233060@gmail.com
#date:2018/10/21 22:09

'''
n个人围成一个圈，从第一个人开始数1，数到第k个出局
然后下一个人继续从1数，求出局人编号
'''
def Joseph(n,k):
    a = [x for x in range(1, n+1)]
    num = k
    for i in range(n):
        print(a[num%len(a)-1])
        del a[num%len(a)-1]
        if len(a)==0:
            print('ok')
        else:
            num = (num + k-1) % len(a)
Joseph(10,2)






