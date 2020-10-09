# TC 2020/10/9/23:25

filename = 'guest.txt'

with open(filename,'w') as file_object:
    while True:
        user_name = input("input your name:(Enter ## to quit)")
        if user_name == '##':
            break
        print("Hello," + user_name.title())
        file_object.write(user_name.title() + '\n')#写成wirte会导致AttributeError
        
