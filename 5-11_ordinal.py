#TC 2020/9/27/11:47

numbers = [x for x in range(1,10)]

for num in numbers:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2rd")
    else:
        print(str(num)+"th")
