"jghghghghghgh"
"jhkjhjjhjhj"
"""jkjkjkjkjkjkjkjkjkjjkjjkjkjkjk😉"""

name = "Alex"
surname = "Bush"
print(id(name))
print(name)

name = name + surname

print(name)
print(id(name))

symbol = "b"
print(ord(symbol))
print(chr(98))

smile = "😉"
print(ord(smile))
print(chr(128521))
print(chr(140000))

heart = "\U00002764jjklkjlkjlkjk"
print(heart)

my_address = "Odesa"
ukraine_country_name = "Ukraine"
PASSWORD = "asddf"

# it is a comment

# adding strings
string_1 = "-------------str1"
string_2 = "str2"
result = string_1 + " " + string_2 + " " + "hjjhjhj"
print(result)

# multiplication
mult_result = string_1 * 2
print(mult_result)

# f strings
result = f"{string_1} {string_2=} hjjhjhj"
print(result)

# templates
WELCOME_TEXT = "Welcome, dear {name}"
result_ilya = WELCOME_TEXT.format(name="Ilya")
result_vasya = WELCOME_TEXT.format(name="Vasja")
print(result_ilya, result_vasya)
