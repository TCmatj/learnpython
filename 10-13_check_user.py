# TC 2020/10/11/22:20

import json

filename = "json\\username.json"
def get_stored_username():
    """如果存储了用户名，就获取它"""
    try:
        with open(filename) as fm:
            username = json.load(fm)
    except FileNotFoundError or json.decoder.JSONDecodeError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?")
    with open(filename,'w') as fm:
        json.dump(username,fm)
    return username

def greet_user():
    """问候用户，并指出其名"""
    thename = input("Enter your name:")
    username = get_stored_username()
    if username == thename:
        print("Welcome back," + username + "!")
    else:
        with open(filename,'w') as fm:
            json.dump(username,fm)
        print("We'll remember you when you come back," + username + "!")

greet_user()