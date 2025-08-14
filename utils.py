import winsound


def make_noise(duration_sec: int = 1) -> None:
    winsound.Beep(frequency=500, duration=duration_sec * 1000)


def get_founder_name() -> str:
    return 'Bill Gates'


def add_two_numbers(number_1: int, number_2: int) -> int:
    add_numbers_result = number_1 + number_2
    return add_numbers_result


def get_people_in_car(passengers: list[str], driver: str = 'Tolik') -> list[str]:
    people_in_car = passengers + [driver]
    return people_in_car


def is_given_name_like_founder_name(given_name: str) -> bool:
    founder_name = get_founder_name()
    is_name_like_founder_name = given_name.lower() == founder_name.lower()
    return is_name_like_founder_name

# passengers = ['you', 'I']
# print(get_people_in_car(passengers, 'Vanya'))
# print(get_people_in_car(passengers, driver='Vanya'))
# print(get_people_in_car(passengers=passengers, driver='Vanya'))
# print(get_people_in_car(driver='Vanya', passengers=passengers))
# print(get_people_in_car( passengers=passengers))
#
# print_result = print(333333333)
# print(print_result)
#
# make_noise()
# make_noise(duration_sec=5)
