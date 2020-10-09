# TC 2020/10/9/0：11

class Restaurant():
    """餐馆类"""

    def __init__(self,name,typ):#双下划线，单下划线引起TypeError: Restaurant() takes no arguments
        """初始化餐馆属性"""
        self.restaurant_name = name
        self.cuisine_type = typ
        self.served_number = 0  #属性默认不需要传参

    def describe_restaurant(self):
        """打印属性"""
        ms = self.restaurant_name + self.cuisine_type
        print(ms)

    def open_restaurant(self):
        print("正在营业")

    def set_number_served(self,number):
        """设置用餐人数"""
        my_restaurant.served_number = number

    def increment_number_served(self,number):
        """每天递增人数"""
        my_restaurant.served_number += number

my_restaurant = Restaurant("YHJTCCY","CHUAN")
print("有{}人在这里用餐".format(my_restaurant.served_number))
my_restaurant.served_number = 199
print("有{}人在这里用餐".format(my_restaurant.served_number))

my_restaurant.set_number_served(88)
print("有{}人在这里用餐".format(my_restaurant.served_number))
my_restaurant.increment_number_served(50)
print("有{}人在这里用餐".format(my_restaurant.served_number))
