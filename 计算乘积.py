n=eval(input("请输入一个数："))
a=1
for i in range(1,n+1):
    a*=i
print("乘积：{}".format(a))