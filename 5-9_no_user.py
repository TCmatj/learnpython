#TC 2020/9/27/11:39

user = ['admin','Eric','TCmatj','OriginYYX','Annan']

if len(user) == 0:
    print("We need to find some users")
else:
    user_name = input('please input your user name:')
    if user_name == 'admin':
        print("Hello admin,would you like to see a status resport?")
    else:
        print("Hello " + user_name + ",thank you for logging in again")
