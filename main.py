import json
import requests


# book_info = {
#     'title': 'Sherlok Holmes',
#     'author': 'Arthur Conan Doyle',
#     'publication_year': 1887,
#     'genres': ['detective', 'novel']
# }
#
# with open('data.json', 'w') as json_file:
#     json.dump(book_info, json_file)


# book_info_str = json.dumps(book_info)
#
# print(book_info_str)


# book_info_str = '{"title": "Sherlok Holmes", "author": "Arthur Conan Doyle", "publication_year": 1887, "genres": ["detective", "novel"]}'
#
# book_info = json.loads(book_info_str)
#
# print(book_info)
# print(type(book_info))

# with open('data.json') as json_file:
#     book_info = json.load(json_file)
#
#     print(book_info)
#     print(type(book_info))


# data - словарь, тип dict
# data = {
#     "name": "John Smith",
#     "age": 30,
#     "city": "New York"
# }
#
# # json_data - строка, тип str, с отступами
# json_data = json.dumps(data, indent=1)
# print(json_data)


# data = {
#     "name": "Иван Иванов",
#     "age": 30,
#     "city": "Москва"
# }
#
# # json_data - строка с не-ASCII символами
# json_data = json.dumps(data, ensure_ascii=True)
# print(json_data)




user = "skypro-008"
url = f"https://api.github.com/users/{user}/repos"

response = requests.get(url)

repos = response.json()

for repo in repos:
    if repo["language"] == "Python":
        print(f"Name: {repo['name']}\nLink: {repo['html_url']}\n")