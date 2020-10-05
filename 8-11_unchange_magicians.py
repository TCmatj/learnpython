# TC 2020/10/5/18:48

def show_magicians(magicians):
    '''打印魔术师名单'''
    for name in magicians:
        print(name)

        
def make_great(un_magi,co_magi):
    '''给魔术师名单加上the Great,并且不改变原列表'''
    for name in un_magi:
        name = 'the Great ' + name
        co_magi.append(name)

        
magicians = ['A','B','C','D']
great_magicians = []
show_magicians(magicians)
make_great(magicians,great_magicians)
show_magicians(magicians)
show_magicians(great_magicians)
