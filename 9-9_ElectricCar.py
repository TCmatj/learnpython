# TC 2020/10/9/10:26

class Car():
    """模拟汽车"""
    def __init__(self,make,model,year):
        self.make = make
        self.model =model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(seld):
        lobg_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odoeter(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles


class Battery():
    """模拟电动汽车电瓶"""

    def __init__(self,battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This  car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
        
        
class ElectricCar(Car):
    """电动汽车独特处"""

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()


my_car = ElectricCar('tesla','model s',2016)
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()
