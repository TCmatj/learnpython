# TC 2020/9/29/23:18

places = []
while True:
    place = input('If you could visit one place in the '
                  + 'world,where would you go?')
    if place.lower() == 'quit':
        break
    places.append(place)
for place in places:
    print(place,end = '  ')
