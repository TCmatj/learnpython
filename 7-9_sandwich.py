# TC 2020/9/29/22:06

sandwich_orders = ['1','2','3','4']
finished_sandwich = []

while sandwich_orders:
    sandwich_work = sandwich_orders.pop()
    print('I made youe ' + sandwich_work + ' sandwich.')
    finished_sandwich.append(sandwich_work)
for finished in finished_sandwich:
    print(finished,end = '   ')
