# TC 2020/9/29/21:35

pizzas = []
pizza = input('输入配料(不再添加配料时输入quit结束添加,不区分大小写）：')
while pizza.lower() != 'quit':
    pizzas.append(pizza)
    print('我们会在披萨中添加：',end = '\n\t')
    for piz in pizzas:
        print(piz,end = '   ')
    print()
    pizza = input('输入配料(不再添加配料时输入quit结束添加）：')
