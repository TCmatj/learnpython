# TC 2020/10/5/18:48

def show_magicians(magicians):
    '''打印魔术师名单'''
    for name in magicians:
        print(name)

        
def make_great(magi):
    '''加上the Great'''
    great = []
    count = 0
    for name in magi:
        magi.pop(count)
        name = 'the Great ' + name
        magi.insert(count,name)
        count += 1

        
magicians = ['A','B','C','D']
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
