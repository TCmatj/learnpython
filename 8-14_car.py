# TC 2020/10/5/19:34

def make_car(manu,model,**car_info):
    '''Make a car'''
    car = {}
    car['manufacture'] = manu
    car['model'] = model
    for key,value in car_info.items():
        car[key] = value
    return car


car = make_car('subaru','outback',color='blue',two_package=True)
print(car)
