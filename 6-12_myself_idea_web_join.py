"""
        TC 2020/9/28/23:35
        v1.0
bug：
    01：密码输入错误一次之后应该不再输入用户名或者给出选择
      需不需要再更改用户名
    02：注册成功后只返回一层while没有立即停止运行程序
可行建议：
    01：把用户字典的值做成嵌套字典，添加密保问题，用于忘记密码时
      做验证，还可以添加个人信息等资料
"""
import time
user_list = {}  #用户字典
test_time = 0   #密码尝试次数

while True:
    temp_name = input("请输入用户名：")  #临时记录输入的用户名
    if temp_name in user_list:
        temp_pass = input("请输入密码：")  #临时记录输入的密码
        test_time += 1
        if user_list[temp_name] == temp_pass:  #用户名密码均正确，登陆成功
            print("登陆成功")
            break;                            #break代替进入网站成功的一系列动作
        else:
            print("第" + str(test_time) + "次密码错误，")
            if test_time == 3:
                test_time =0
                print("密码错误次数达到三次，请等待30秒后再试")
                time.sleep(30)
    else:
        test_status = input("未建立的用户名，请仔细检查用户名是否输入错误\n"
                            + "用户注册输入yes，重新输入用户名输入re\n"
                            + "否则将退出系统:")
        if test_status == 're':
            continue
        elif test_status == 'yes':
            while True:
                temp_init = input("注册用户名：")
                if temp_init not in user_list:     #用户名不存在可以注册
                    temp_initpass = input("注册密码")
                    user_list[temp_init] = temp_initpass
                    print("登陆成功")
                    break;
                else:
                    print("用户名已存在")          #用户名已存在不能注册
        else:
            break
