# TC 2020/10/9/11:00
"""
    可变参数会转换成元组
    多次使用可变参数只需要开始转换为元组即可
    后面再加*会变为嵌套元组
"""

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

class Admin(User):
    """管理员类"""

    def __init__(self,first_name,last_name,*info,**other):
        super().__init__(first_name,last_name,**other)
        self.privileges = Privileges(info)
 
class Privileges():
    """权限类"""

    def __init__(self,others):
        """*other 错误传递
        原因：Admin类已经将info转换为元组
        再加*会转换成嵌套的元组
        """
        self.privileges = ["can add post","can delete post","can ban user"]
        for other in others:
            self.privileges.append(other)

    def show_privileges(self):
        print("You have they privileges:")
        for privilege in self.privileges:
            print(" -- " + privilege)
