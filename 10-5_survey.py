# TC 2020/10/10/00:06

from os import path

filename = 'why_like_code.txt'
flienum = 'number.txt'

with open(filename,'a') as file_object:
    with open(flienum,'r') as num:
        number = num.read()
    while True:
        if type(number) is int:    #类型判断int说明已经转换过格式了
            pass
        elif not path.getsize(flienum): #初次运行初始化number
            number = 1
        else:
            number = int(number) #字符转整数
        reason = input("Why you like code?:(Enter ## to quit)")
        if reason == '##':
            break
        file_object.write('reason{}:'.format(number) + reason + '\n')
        number += 1
    with open(flienum,'w') as num:
        num.write(str(number))
