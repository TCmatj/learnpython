# TC 2020/10/5/19:16

def sandwich(size,*materials):
    '''Make a sandwich'''
    print("Making a ",size,'-inch sandwich with the following toppings:',sep='')
    for material in materials:
        print('-',material)

        
sandwich(12,'tomato')
sandwich(14,'tomato','Bocan',"cheese")
sandwich(18)
