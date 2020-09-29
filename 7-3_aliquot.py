# TC 2020/9/29/21:24

number = int(input('请输入一个数，以便判断它是不是7的倍数：'))
time = int(number / 7)
remainder = number % 7
if remainder == 0:
    print('被7整除得：' + str(time))
else:
    print('被7除得：' + str(time) + ' ,余：' + str(remainder))
