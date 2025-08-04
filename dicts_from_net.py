import requests
from pprint import pprint

url = 'https://dummyjson.com/todos'
params = {
    'limit': 1000,
    'skip': 0
}


response = requests.get(url, params=params)
# print(response.content)
# print(response.text)
# print(response.json())
# pprint(response.json())

response_json = response.json()
todos = response_json['todos']

search_word = 'in'
search_result = []
search_word_count = 0

users_todos = {}


group_by_completed = {
    True: [],
    False: [],
}


uncompleted = []
for todo in todos:

    group_by_completed[todo['completed']].append(todo)

    if not todo['completed']:
        uncompleted.append(todo)

    if search_word in todo['todo'].lower():
        search_result.append(todo)
        search_word_count += 1

    if todo['userId'] not  in users_todos:
        users_todos[todo['userId']] = [todo]
    else:
        users_todos[todo['userId']].append(todo)

print(f'{len(search_result)=}')
print(f'{search_word_count=}')
# pprint(group_by_completed)
# pprint(users_todos)
# pprint(search_result)
# pprint(uncompleted)
pass
