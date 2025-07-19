some_string = 'ä	ö	ü	 	ßn      i liVe 0000in Odesa cit998787878799y                     '
some_string2 = 'ä	ö	ü	 	SSN      i liVe 0000in Odesa cit998787878799y                     '

# print(
#     some_string,
#
#     some_string.count('live'),  # number
#
#     some_string.lower(),
#     some_string.upper(),
#     some_string.title(),
#     some_string.strip(),
#     some_string.lstrip(),
#     some_string.rstrip(' y'),
#
#     sep='\n'
# )
#
# # editing
#
# some_string_replaced = some_string.replace('i', 'I', 2).replace('O', 'A')
# print(some_string_replaced)


# bad idea
# some_string_replaced2 = some_string.replace('i', 'a' ).replace('a', 'B').replace('9', '')
# print(some_string_replaced2)

# table = str.maketrans('ia', 'aB', '9')
# table = str.maketrans('ia0', 'aB1', '987l')
# translated = some_string.translate(table)
# print(translated)


# print(
#     some_string.title(),
#     some_string.capitalize(),
#     sep='\n'
# )


# print(
#     some_string.upper() == some_string2.upper(),
#     some_string.casefold(),
#     some_string.upper(),
#     some_string.lower(),
#     some_string,
#     sep='\n'
# )


# name = 'Alex'
#
# print(
#     name.center(21, '-'),
#     name.ljust(21, '-'),
#     name.rjust(21, '0'),
#     sep='\n'
# )
#
# print(
#     name.swapcase(),
#     name.zfill(21),
#
#     sep='\n'
# )
#
# result = (
#     some_string.lower()
#     .zfill(250)
#     .replace('5', '7')
# )

poem = """
Мені тринадцятий минало.
Я пас ягнята за селом.
Чи то так сонечко сіяло,
Чи так мені чого було?
Мені так любо, любо стало,\\n
Неначе в бога. .......
Уже прокликали до паю,
А я собі у бур'яні
Молюся богу... І не знаю,
Чого маленькому мені
Тоді так приязно молилось,
Чого так весело було?
Господнє небо і село,
Ягня, здається, веселилось!
І сонце гріло, не пекло!
"""

# poem = "  \n\n\tМені тринадцятий минало.\nЯ пас ягнята за селом.\nЧи то так сонечко сіяло,"
print(poem.strip())
