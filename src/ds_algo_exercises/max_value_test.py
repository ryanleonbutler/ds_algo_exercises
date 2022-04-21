import pytest

from ds_algo_exercises.max_value import max_value

@pytest.mark.parametrize(
    "nums, expected_result",
    [
        ([4, 7, 2, 8, 10, 9], 10),
        ([10, 5, 40, 40.3], 40.3),
        ([-5, -2, -1, -11], -1),
        ([42], 42),
        ([1000, 8], 1000),
        ([1000, 8, 9000], 9000),
        ([2, 5, 1, 1, 4], 5),
    ],
)

def test_returning_max_value(nums, expected_result):
    assert max_value(nums) == expected_result
    
