# TC 2020/10/8/21:57

class Restaurant():
    """餐馆类"""

    def __init__(self,name,typ):#双下划线，单下划线引起TypeError: Restaurant() takes no arguments
        """初始化餐馆属性"""
        self.restaurant_name = name
        self.cuisine_type = typ

    def describe_restaurant(self):
        """打印属性"""
        ms = self.restaurant_name + self.cuisine_type
        print(ms)

    def open_restaurant(self):
        print("正在营业")

my_restaurant = Restaurant("YHJTCCY","CHUAN")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
