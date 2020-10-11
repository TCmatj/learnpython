# TC 2020/10/11/21:48

import json

filename = 'json\\like_number.json'

try:
    with open(filename) as fm:
        number = json.load(fm)
except FileNotFoundError or json.decoder.JSONDecodeError: 
    #文件不存在或者json文件为空
    with open(filename,'w') as fm:
        number = input("Input your favorite number:")
        json.dump(number,fm)
else:
    print("I know your favorite number!It's {}.".format(number))