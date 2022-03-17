# 从键盘输入一个年份，判断此年份是闰年还是平年。 例如：1987：平年；1984：闰年；1900：平年；2000：闰年
year=input("请输入一个年份：")
if ((eval(year)%4==0 and eval(year)%100!=0) or (eval(year)%400==0)):
    print("闰年")
else:
    print("平年")
