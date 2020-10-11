# TC 2020/10/11/21:48

import json

filename = 'json\\like_number.json'

with open(filename,'r') as fm:
    number = json.load(fm)
    print("I know your favorite number!It's {}.".format(number))