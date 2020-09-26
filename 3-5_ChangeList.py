#TC 2020/9/24/9:48

persons=['tc','orgin','anan','huangliang']

for person in persons:

    print('Can '+person.title()+' come to dinner?')

print("\nHuangliang can't come to dinner.\n")

persons[-1]='Hl'

for person in persons:

    print('Can '+person.title()+' come to dinner?')
