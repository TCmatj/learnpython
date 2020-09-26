"""
TC
2020/9/25/11:39
"""
language=[]

#插入
print('插入/添加:append\insert方法')
language.append('C')
print(language)
language.insert(1,'Python')
print(language)
language.insert(1,'Java')
print(language)
language.append('C++')
print(language)


#删除
##del language[1]#删除第二项
##print(language)
##del language[1:]#删除第二项之后/切片
##print(language)

##temp=language.pop()#弹出栈顶元素
##print(language)
##print(temp)
##temp=language.pop(2)#弹出第3项
##print(language)
##print(temp)

##language.remove('Java')
##print(language)


#排序
print('sorted:\n',sorted(language))#临时排序，函数，需要将参数放里边
print(language)

print('sorted+reverse:\n',sorted(language,reverse=True),sep='abc')
print(language)

print('reverse:\n',end='')
language.reverse()
print(language)

language.reverse()
print(language)

print('sort:')
language.sort()#排序,方法，写在需要操作的项目之后
print(language)
language.sort(reverse=True)
print(language)
