# TC 2020/10/4/23:09

def make_album(name,album,num=''):
    message = {'name':name,'album':album}
    if num == '':
        return message
    else:
        message['total'] = num
        return message
print(make_album('Jone','123',12))
print(make_album('Steck','456'))
print(make_album('Pens','789',8))
