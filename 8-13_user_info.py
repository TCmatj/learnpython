# TC 2020/10/5/19:27

def build_profile(first,last,**user_info):
    """创建一个字典，包括我们所知的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('TC','matj',QQ=2216685752,
                             country='China',age=21)
print(user_profile)
