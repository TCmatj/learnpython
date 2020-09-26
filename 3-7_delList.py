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

print("\nThe dining-table can't carry here,so,sorry I can,only,let two persons join.\n")

for i in range(1,5):

    pop_person=persons.pop()

    print(str(i)+'\t'+pop_person.title()+',Sorry,I am can not let you join my dinner.')
    
i=1

for person in persons:

    print(str(i)+'\t\t'+person.title()+',You in the list of dinner yet.')
    
    i=i+1

del persons[2]

print(persons)

del persons[1]

print(persons)

del persons[0]

print(persons)
