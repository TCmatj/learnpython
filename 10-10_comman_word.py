# TC 2020/10/10/23:28

with open("Pride_and_Prejudice.txt",'rb') as fm:
    pride = fm.read()
    print(pride.count(86))