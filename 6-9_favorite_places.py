# TC 2020/9/28/23:03

favorite_places = {
    'origin':['Hangzhou','nanjing','taiyuan'],
    'tc':['jiujiang','wuxi','nanjing'],
    'baby':['wuxi','zhengzhou'],
    }
for name,places in favorite_places.items():
    print(name.title())
    print('\t',end = '')
    for place in places:
        print(place.title(),end = ' ')
    print()
