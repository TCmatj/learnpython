#TC 2020/9/24/9:48

persons=['tc','orgin','anan','huangliang']

i=1

for person in persons:

    print(str(i)+'\tCan '+person.title()+' come to dinner?')
    
    i=i+1

print("\nI am find a big dining-table.\n")

persons.insert(0,'HL')

persons.insert(int(len(persons)/2),'AN')

persons.append('hz')

i=1

for person in persons:

    print(str(i)+'\tCan '+person.title()+' come to dinner?')

    i=i+1
