
# with open('people.csv', mode='w', encoding='utf-8') as file:
#     file.write('number;name;age\n')
#     file.write('1;Alex;23\n')
#     file.write('2;Bob;22\n')
#     file.write('3;Marta;12\n')
#     file.write('4;John;10\n')
#     file.write('5;Sean;15\n')


# with open('people.csv', mode='a', encoding='utf-8') as file:
#     file.write('6;John;10\n')
#     file.write('7;Sean;15\n')

# with open('people.csv', mode='r', encoding='utf-8') as file:
#     rows = file.readlines()
#     for row in rows[1:]:
#         print(row, end='')
#         number, name, age = row.strip().split(";")
#         print(number, name, age)

# do this way !!!!!!!!!!!!!!!!!!!!
import csv
# with open('people.csv', mode='r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     print(reader)
#     for row in reader:
#         print(row)

# with open('people.csv', mode='r', encoding='utf-8', newline='') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     print(reader)
#     for row in reader:
#         print(row)

user_data = [
    ['name', "gender", 'age'],
    ['Alex', "male", '15'],
    ['Marta', "female", '18'],
    ['Sean', "male", '23'],
]

# with open('people_write.csv', mode='w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerows(user_data)
#     writer.writerow(['Sean', "male", '45'])

user_data_json = [
    {"name": "Alex", 'age': 15, 'gender': "male"},
    {"name": "Sean", 'age': 25, 'gender': "male"},
    {"name": "Marta", 'age': 18, 'gender': "female"},
    {"name": "Alex",  'gender': "male"},
]

with open('people_write2.csv', mode='w', encoding='utf-8', newline='') as file:
    fieldnames = ['name', 'age', "gender"]
    writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(user_data_json)