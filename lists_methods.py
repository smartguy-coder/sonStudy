dads_list = ['Bread', 'salt', 'matches']
grandson_list = ['butter', 'ice-cream']

grandson_list.append('napkins')

bogdan_list = ['candies', 'spaghetti', 'cookies']
grandson_list.extend(bogdan_list)
# grandson_list.extend('napkins')


final_list = dads_list + grandson_list
print(final_list)
final_list.sort(reverse=True)
final_list.reverse()
print(final_list)

print(final_list[::3])
print(final_list[::-2])

# final_list.insert(1, 'sugar')
# print(final_list)

final_list[1] = 'sugar'
final_list[2] = 'sugar'

# delete

# final_list.remove('candies')
last = final_list.pop()
last = final_list.pop(3)
print(last)

del final_list[0]
del final_list[3:]


# final_list

print(
    len(final_list),
    len(final_list[0]),
    final_list.index('sugar'),
    'sugar' in final_list,
    final_list.count('sugar')
)

print(final_list)


