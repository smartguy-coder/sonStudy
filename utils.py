import winsound
import statistics


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


def get_average(numbers: list[float]) -> float:
    return statistics.fmean(numbers)


def is_correct_triangle(side_1: float, side_2: float, side_3: float) -> bool:
    for side in (side_1, side_2, side_3):
        if side <= 0:
            return False
    correct_length_1_2 = side_1 + side_2 > side_3
    correct_length_1_3 = side_1 + side_3 > side_2
    correct_length_2_3 = side_3 + side_2 > side_1
    return correct_length_1_3 and correct_length_1_2 and correct_length_2_3


def get_triangle_perimeter(side_1: float, side_2: float, side_3: float) -> float:
    if not is_correct_triangle(side_1, side_2, side_3):
        raise ValueError("wrong triangle data")
    perimeter = side_1 + side_2 + side_3
    return perimeter
