# TC 2020/9/28/22:14

vocabulary={'set':'集合，集合中的元素不会重复，其它性质与字典相同',
            '.title()':'标题格式：首字母大写','.upper()':'全部大写',
            'list':'列表，可以进行的部分操作：list.append();list.insert(-1,\'d\');list.pop(可选择参数)',
            'sorted':'临时排序，不改变原来的顺序，只是临时改变可选参数：reverse = True，倒叙',
            }
for key,value in vocabulary.items():
    print(key)
    print('\t'+value)
