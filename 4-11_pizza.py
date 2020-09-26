#TC 2020/9/25/21:50

pizzas=['必胜客','棒约翰','笨蛋牌','宝宝牌']

friend_pizzas=pizzas[:]

pizzas.append('Y')
friend_pizzas.append('X')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza,end=' ')
print('\nMy friend\' favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza,end=' ')
