import requests
import pygal

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()

print("Total repositories:",response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))

r_dicts = []
# 研究仓库
for repo_dict in repo_dicts:
    temp_dict = []
    temp_dict.append(repo_dict['name'])
    temp_dict.append(repo_dict['stargazers_count'])
    temp_dict.append(repo_dict['owner']['login'])
    temp_dict.append(repo_dict['html_url'])
    temp_dict.append(repo_dict['created_at'])
    temp_dict.append(repo_dict['updated_at'])
    temp_dict.append(repo_dict['language'])
    temp_dict.append(repo_dict['description'])
    r_dicts.append(temp_dict)
pic = pygal.Bar()
pic.title = "Stars count"
x_table,y_table = [],[]
for value in r_dicts:
    x_table.append(value[0])
    y_table.append(value[1])
pic.x_labels = x_table
pic.x_title = "Repository name"
pic.y_title = "Star number"
pic.add("Star",y_table)
pic.render_to_file('./chapter17/py_repos.svg')