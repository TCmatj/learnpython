# TC 2020/9/28/22:31

rivers = {'nile':'egypt','yabgtze river':'china','mississippi river':'us'}
for river,country in rivers.items():
    if(country.lower() == 'us'):
        print('The ' + river.title() + ' runs through ' + country.upper() + '.')
    else:
        print('The ' + river.title() + ' runs through ' + country.title() + '.')
