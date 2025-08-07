# create file

# file = open('text_file.txt', mode='w', encoding='utf-8')
# print(file)
# 1/0
# file.close()

# with open('text_file.txt', mode='w', encoding='utf-8') as file:
#     file.write('gjdhgffffffffffffd\nhgkjdfhgkjdfhgjkdf111')

    # file.write('gjd5555ffffd\nhgkjdfhgkjdfhgjkdf111')

with open('text_file2.txt', mode='a', encoding='utf-8') as file:
    file.write('gjdhgf\tfffffffffffd\nhgkjdfhgkjdfhgjkdf111')

# read file
# with open('text_file2.txt', mode='r', encoding='utf-8') as file:
#     data = file.read()
#     print(data)

#
# with open('text_file2.txt', mode='r', encoding='utf-8') as dragon:
#     data = dragon.readlines()
#     print(data)


# with open('text_file2.txt', mode='r', encoding='utf-8') as dragon:
#     line_1 = dragon.readline()
#     print(line_1, end='')
#     line_2 = dragon.readline()
#     print(line_2)
#     line_3 = dragon.readline()
#     print(line_3)
#     dragon.seek(30)
#     next_line = dragon.readline()
#     print(next_line, end='')
# print(dragon.readline())