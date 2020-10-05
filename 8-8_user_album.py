# TC 2020/10/4/23:16

def make_album(name,album,num=''):
    '''创建专辑'''
    message = {'name':name,'album':album}
    if num == '':
        return message
    else:
        message['total'] = num
        return message

    
while True:
    name = input('输入歌手名称：(退出输入q)')
    if name == 'q':
        break
    album = input('输入歌手专辑：(退出输入q)')
    if album == 'q':
        break
    num = input('专辑歌曲数量：(退出输入q)')
    if num == 'q':
        break
    print(make_album(name,album,num))
    
