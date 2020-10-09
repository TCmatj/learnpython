# TC 2020/10/9/22:43

filename = 'C:\\Users\\Administrator\\Desktop\\learnpython\\python_study.txt'

##with open(filename) as file_object:
##    contents = file_object.read()
##    print(contents)
##    contents = contents.replace('Python','C')
##    print(contents)

##with open(filename) as file_object:
##   for line in file_object:
##       print(line.rstrip())
with open(filename) as file_object:
    contents = file_object.readlines()
for line in contents:
    line = line.replace('Python','C') #replace方法不改变原来的字符串
    print(line.rstrip())
