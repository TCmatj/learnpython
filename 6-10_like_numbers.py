# TC 2020/9/28/23:11

numbers = {'originyyx':[5,8],
           'baby':[0,9],
           'annan':[7,1],
           'me':[9,1],
           'huangliang':[7,6],
           }
for name,number in numbers.items():
    print('\n' + name.title())
    for num in number:
        print('   ' + str(num),end = ' ')
    
