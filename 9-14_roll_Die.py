# TC 2020/10/9/11:26

from random import randint

class Die():
    """骰子类，默认6面"""
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))

die1 = Die(10)
die2 = Die(20)

for i in range(1,11):
    print("{}:".format(i),end = '')
    die1.roll_die()
for i in range(0,20):
    print("{}:".format(i+1),end = '')
    die2.roll_die()
