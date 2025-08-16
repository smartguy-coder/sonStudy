import pytest

import utils


def test_get_triangle_perimeter_1():
    side_1 = 3
    side_2 = 4
    side_3 = 5
    expected_result = 12
    actual_result = utils.get_triangle_perimeter(side_1, side_2, side_3)
    assert actual_result == expected_result


def test_get_triangle_perimeter_2():
    side_1 = 3
    side_2 = 4
    side_3 = 10
    with pytest.raises(ValueError):
        utils.get_triangle_perimeter(side_1, side_2, side_3)



def test_is_correct_triangle_1():
    side_1 = 3
    side_2 = 4
    side_3 = 10
    actual_result = utils.is_correct_triangle(side_1, side_2, side_3)
    assert actual_result is False


def test_is_correct_triangle_2():
    side_1 = 3
    side_2 = 4
    side_3 = 5
    actual_result = utils.is_correct_triangle(side_1, side_2, side_3)
    assert actual_result is True


def test_is_correct_triangle_3():
    side_1 = -3
    side_2 = 4
    side_3 = 5
    actual_result = utils.is_correct_triangle(side_1, side_2, side_3)
    assert actual_result is False


@pytest.mark.parametrize(
    'side_1, side_2, side_3, expected_result',
    [
        (3, 4, 10, False),
        (3, 4, 5, True),
        (-3, 4, 5, False),
    ]
)
def test_is_correct_triangle_general(side_1, side_2, side_3, expected_result: bool):
    actual_result = utils.is_correct_triangle(side_1, side_2, side_3)
    assert actual_result is expected_result















