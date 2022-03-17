import random
s=0
for i in range(5):
    a=random.randint(1,100)
    b=random.randint(1,100)
    c=eval(input("{}+{}=".format(a,b)))
    if c==a+b:
        s+=1
if s>=4:
    print("最后得分：{} 闯关成功".format(s))
else:
    print("最后得分：{} 闯关失败".format(s))