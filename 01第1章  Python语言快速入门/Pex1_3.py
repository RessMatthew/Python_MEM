# 程序文件Pex1_3.py 计算1+2+...+7并输出
_sum = 0
number = int(input("请输入整数："))
print("从小到大排列输出数字：")
for i in range(1, number + 1):
    _sum += i  # 设置sum为i的和
    print("%d" % i, end='')
    if i < number:
        print("+", end='')  # 设置输出连加的算式
    else:
        print("=", end='')
print("%d" % _sum)
_sum = 0
print("从大到小排列输出数字：")
for i in range(number, 0, -1):
    _sum += i  # 设置sum为i的和
    print("%d" % i, end='')
    if i > 1:
        print("+", end='')  # 设置输出连加的算式
    else:
        print("=", end='')
print("%d" % _sum)
