#TC 2020/9/25/22:33

number=[]

for count in range(3,31):
    if count%3==0:
        number.append(count)
        #number.insert(-1,count)#行不通
print(number)
