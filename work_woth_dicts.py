name = 'Alex'
surname = 'Bush'

my_info = {}

user = {
    'name': 'Alex',
    'name': 'Bill',
    'surname': 'Bush',
    'age': 45,
    'money': 250.36,
    'hobbies': [
        'tennis', 'soccer'
    ],
    'address': {
        'city': 'Odesa',
        'street': 'Main',
    },
    0: True,
}

another_user = {'name': 'John', 'surname': 'Schmidt', 'hobbies': []}

# for key in user:
#     print(key)
#     print(user[key])
#     print('*' * 20)

# print(user.keys())
# for key in user.keys():
#     print(key)

# print(user.values())
# for value in user.values():
#     print(value)

strrr = ('kdfh'
         'gjkdfkgdf'),
print(strrr)

tuple_example = 5, 10
print(tuple_example)
print(len(tuple_example))
print(tuple_example[0])
print(55 in tuple_example)
# tuple_example[0] = 66
first, second = tuple_example
print(first)
print(second)

print(user.items())
for key, value in user.items():
    print(value)