# TC 2020/10/9/11:08
import onlyuser

class Admin(onlyuser.User):
    """管理员类也需要写成 文件名.类名"""

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
