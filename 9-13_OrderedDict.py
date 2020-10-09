# TC 2020/10/9/11:15

from collections import OrderedDict
vocabulary = OrderedDict()
vocabulary['set'] = '集合，集合中的元素不会重复，其它性质与字典相同'
vocabulary['.title()'] = '标题格式：首字母大写'
vocabulary['.upper()'] = '全部大写'
vocabulary['list'] = '列表，可以进行的部分操作：list.append();list.insert(-1,\'d\');list.pop(可选择参数)'
vocabulary['sorted'] = '临时排序，不改变原来的顺序，只是临时改变可选参数：reverse = True，倒序'
for key,value in vocabulary.items():
    print(key)
    print('\t'+value)
