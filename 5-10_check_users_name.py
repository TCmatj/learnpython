#TC 2020/9/27/11:40


current_users = ['admin','eric','tcmatj','originyyx','annan']
new_users = ['admin','Frank','Susan','TCmatj','TC2020']

for name in new_users:
    if name.lower() in current_users:
        print("The user name has been used.")
    else:
        print("The user name is not used.")
