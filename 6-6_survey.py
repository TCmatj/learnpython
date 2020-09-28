# TC 2020/9/28/22:42

favorite_language = {
    'jen':'python',
    'sarch':'c',
    'edward':'ruby',
    'phil':'python',
    }
nonlist = ['origin','jen','edward','TC']
for person in nonlist:
    if person in favorite_language:
        print('Thank you,' + person.title() +',for your help!')
    else:
        print(person.title() + ',invite you to participate in the survey.')
