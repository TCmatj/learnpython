# TC 2020/9/29/23:06

sandwich_orders = ['1','2','3','4','pastrami','pastrami','pastrami']
finished_sandwich = []

while sandwich_orders:
    sandwich_work = sandwich_orders.pop()
    if sandwich_work == 'pastrami':
        print('No pastrami')
    else:
        print('I made youe ' + sandwich_work + ' sandwich.')
        finished_sandwich.append(sandwich_work)
for finished in finished_sandwich:
    print(finished,end = '   ')
