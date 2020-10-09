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

class IceCreamStand(Restaurant):
    """冰淇淋类"""

    def __init__(self,name,typ,*flavors):
        super().__init__(name,typ)
        self.flavors = ['草莓味','巧克力']
        for flavor in flavors:
            self.flavors.append(flavor)

    def print_ice_cream(self):
        for flavor in self.flavors:
            print(flavor)

icecream = IceCreamStand("TC","Ice","芒果布丁")
icecream.print_ice_cream()
