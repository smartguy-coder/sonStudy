import string
import getpass


# string1 = '   \n   '
# maybe_punctuation = '/'
#
# print(
#     maybe_punctuation in string.punctuation
# )
#
#
# print(
#     string1.isdigit(),
#     string1.isascii(),
#     string1.isalnum(),
#     string1.isalpha(),
#     string1.islower(),
#     string1.endswith('5'),
#     string1.startswith('f'),
#     string1.istitle(),
#     string1.isspace()
# )

LOGIN = 'admin'
PASSWORD = '123'

user_login = input("Enter your login: ")
user_password = getpass.getpass("Enter your password: ")
print(user_password)

if LOGIN == user_login and PASSWORD == user_password:
    print('))))))))))))))))))))))')
