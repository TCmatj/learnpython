# TC 2020/10/9/23:25

filename = 'guest.txt'

user_name = input("input your name:")
with open(filename,'w') as file_object:
    file_object.write(user_name)#写成wirte会导致AttributeError
