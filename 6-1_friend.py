# TC 2020/9/28/21:46

originyyx = {'first_name':'yang','last_name':'xiyu','age':23,'city':'杭州'}
print(originyyx['first_name'])
print(originyyx['last_name'])
print(originyyx['age'])
print(originyyx['city'])
for key in originyyx:
    print(key)
for key,value in originyyx.items():
    print(key+': '+str(value))
for key in originyyx.keys():
    print(key)
