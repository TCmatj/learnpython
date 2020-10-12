# TC 2020/10/12/10:49

def city_info(city,country,population=''):
    """格式化城市属性"""
    if population == '':
        ms = city.title() + ',' + country.title()
    else:
        ms = city.title() + ',' + country.title() + " - population {}.".format(population)
    return ms