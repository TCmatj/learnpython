# TC 2020/10/6/22:50

"""
    Pyhon无师自通
    游戏--Hangman
"""

import random

word_list = ['love','python','broad','format','fast','wrong']

def hangman(word):
    wrong = 0                           #错误次数
    stages = ["",
              "________       ",
              '|      |       ',
              '|      |       ',
              '|      0       ',
              '|     /|\      ',
              '|     / \      ',
              '|              ',
              ]
    rletters = list(word)               #将单词存入列表
    board = ["_"]*len(word)             #猜测单词状态，使用_代替未被猜出的字母
    win = False
    print("Welcome to Hangman")
    while wrong<len(stages) - 1:
        print('\n')
        msg = "Guess a letter\n"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char) #获取第一个匹配字母的索引
            board[cind] = char          #字母被猜出，改变相应索引处单词状态
            rletters[cind] = '$'        #已经猜到的字母改为 $ 状态
        else:
            wrong +=1
        print((" ".join(board)))        #打印猜测进度
        e = wrong + 1
        print("\n".join(stages[:e]))    #打印吊起人的状态
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[:]))
        print("You lose!It was {}.".format(word))

hangman(word_list[random.randint(0,5)])
