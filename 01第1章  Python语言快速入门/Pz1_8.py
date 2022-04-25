# 程序文件Pz1_8.py
_sum = 0
number = 1
while True:
    if number == 0:
        break
    number = int(input("数字0结束程序，请输入数字："))
    _sum += number
print("目前累加的结果为：%d" % _sum)
