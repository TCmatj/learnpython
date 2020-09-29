# TC 2020/9/29/21:42

active = int(input('输出要询问的次数：'))
while active > 0:
    age = input('输入年龄：')
    if age.lower() == 'quit':
        break
    else:
        age = float(age)
    if age > 12:
        print('票价：15美元')
    elif age >= 3:
        print('票价：10美元')
    elif age >= 0:
        print('免费')
    else:
        print('请重新输入正确的年龄')
    active -= 1
