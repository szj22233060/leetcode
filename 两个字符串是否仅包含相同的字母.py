#coding=utf-8
#milo22233060@gmail.com
#2018/11/1 10:17

from itertools import combinations

def judge():
    s1 = set(input())
    s2 = set(input())
    print(s1,s2)
    if len(s1) != len(s2):
        return False
    for i in s1:
        print(i)
        if i not in s2:
            return False
    return True
print(judge())
















