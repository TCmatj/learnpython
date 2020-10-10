# TC 2020/10/10/22:59

cats = '.\\txt\\cats.txt'
dogs = '.\\txt\\dogs.txt'

try :
    with open(cats,'r') as cat:
        cat_names = cat.readlines()
except FileNotFoundError:
    print("Sorry,the file " + cats +" does not exist.")
else:
    for cat_name in cat_names:
        print(cat_name.rstrip())
try :
    with open(dogs,'r') as dog:
        dog_names = dog.readlines()
except FileNotFoundError:
    print("Sorry,the file " + dogs +" does not exist.")
else:
    for dog_name in dog_names:
        print(dog_name.rstrip())