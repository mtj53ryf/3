# 输入一元二次方程ax**2+bx+c=0的a，b，c，求两个根，不考虑虚数解。
import math

a=eval(input("请输入a："))
b=eval(input("请输入b："))
c=eval(input("请输入c："))


def quadratic(a, b, c):
    key=b**2-4*a*c
    if key>0:
        x1=(-b+math.sqrt(key))/(2*a)
        x2=(-b-math.sqrt(key))/(2*a)
    if key==0:
        x1=-b/(2*a)
        x2=x1
    if key<0:
        print('方程无解')
        return (None, None)
    return (x1,x2)


print(quadratic(a,b,c))
