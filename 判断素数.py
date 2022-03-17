# 给定一个整数，判断是否是素数，素数是一个只能被1和自身整除的正整数。
from math import sqrt

a=eval(input("请输入一个数："))
k=sqrt(a)
for b in range(2,int(k+1)):
    if (a%b==0):
        print("这个数不是素数。")
        break
    if (b==int(k)):
        print("这个数是素数。")
