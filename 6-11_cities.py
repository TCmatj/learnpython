# TC 2020/9/28/23:17

cities = {
    'nanjing':{
        'country':'china',
        'population':8506000,
        'fact':'The Rape of Naking',
        },
    'new york':{
        'country':'us',
        'population':8537673,
        'fact':"September 11 attacks",
        },
    'tokyo':{
        'country':'japan',
        'population':13617445,
        'fact':"Nisen Niju-nen Kaki Orinpikku",
        },
    }

for city_name,city_info in cities.items():
    count = len(city_info)
    print('\n' + city_name.title(),end = '\n   ')
    for key in city_info:
        print(key + ': ' + str(city_info[key]))
        if count > 0:
            print('   ',end = '')
    
