# TC 2020/10/11/21:39

import json

filename = 'json\\like_number.json'

number = int(input("输入喜欢的数字："))
with open(filename,'w') as fm:
    json.dump(number,fm)