import utils


def test_get_average_1():
    numbers = [55, 55, 55]
    expected_result = 55.0
    actual_result = utils.get_average(numbers=numbers)
    print(2222222222222222222222222222)
    assert actual_result == expected_result


def test_get_average_2():
    numbers = [0, 1, 11]
    expected_result = 4.0
    actual_result = utils.get_average(numbers=numbers)
    assert actual_result == expected_result
