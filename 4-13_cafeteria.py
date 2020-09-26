#TC 2020/9/25/23:28

food_list=('干锅豆腐','查干','白菜','肉汤','烧烤')
count=0
for food in food_list:
    count+=1
    if count!=5:
        print(food,end=' ')
    else:
        print(food)

food_list=('干锅豆腐','查干','白菜','麻婆豆腐','青椒炒蛋')
for food in food_list:
    count+=1
    if count!=10:
        print(food,end=' ')
    else:
        print(food)
