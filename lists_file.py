some_string = '111 222 333 444 555'
print(
    some_string.split('333'),
    some_string.split(),
)

s = (f'lkg'
     f'hbjkfg')
print(s)

my_roommates = []
my_hobbies = [
    '1 tennis',
    '2 pin-pong',
    '3 soccer',
    'pin-pong',
    'soccer',
    'pin-pong',
    'soccer last',
]

concatenated_hobbies = '; '.join(my_hobbies)
concatenated_hobbies = '; '.join('mkghjgjhgjghjgjgj')
print(concatenated_hobbies)

print(my_hobbies)

numbers = [1, 2, 3]
words = ['apple', 'car']
mixed = [1, 'word', 2.55, True, False]
print(id(my_hobbies))
print(id(my_hobbies[:]))

print(
    my_hobbies[0],
    my_hobbies[3],
    my_hobbies[-1],
    my_hobbies[-3],
    my_hobbies[2:3+2],
    some_string[2:3+2],
    some_string[:10],
    sep="\n"
)


