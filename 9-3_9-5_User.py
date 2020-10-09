# TC 2020/10/8/22:27

class User():
    """用户类
       first_name();last_name();greet_user()
    """
    def __init__(self,first_name,last_name,**other):
        """初始化:other其它信息字典"""
        self.other = {}                 #对传入字典处理时要定义空字典
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        for key,value in other.items(): # 字典处理方法忘记
            self.other[key] = value

    def describe_user(self):
        """描述用户属性"""
        ms = " - Name: " + self.first_name.title() + " " + self.last_name.title()
        print(ms)
        print(' - login attempts: ' + str(self.login_attempts))
        for key in self.other:
            print(" - " + key.title() + ": " +str(self.other[key]))#键值为数字时转换为字符串

    def great_user(self):
        """问候用户"""
        name = self.first_name.title() + " " + self.last_name.title()
        print("你好，" + name + "，欢迎登陆")

    def increment_login(self):
        self.login_attempts += 1
        
    def reset_login(self):
        self.login_attempts = 0

users = []
tc = {'hobit':'learn-C/C++/Python'}
yyx = {"number":3,"hobit":"C++"}
yhj = {'hobit':'picture'}
users.append(User('TC','mtj',**tc))     #列表添加数据不能直接赋值
users.append(User('YYX','origin',**yyx))#使用参数的方法注意
users.append(User('Y','hj'))

for i in range(0,3):
    print("User{},infomation:".format(i+1))
    users[i].increment_login()
    users[i].describe_user()
    users[i].great_user()
    print("\n")
for i in range(0,3):
    print("User{},infomation:".format(i+1))
    users[i].increment_login()
    users[i].describe_user()
    users[i].great_user()
    print("\n")
users[0].reset_login()
for i in range(0,3):
    print("User{},infomation:".format(i+1))
    users[i].increment_login()
    users[i].describe_user()
    users[i].great_user()
    print("\n")
