import pytest

from ds_algo_exercises.pair_sum import pair_sum


@pytest.mark.parametrize(
    "numbers, target_sum, expected_result",
    [
        ([3, 2, 5, 4, 1], 8, (0, 2)),
        ([4, 7, 9, 2, 5, 1], 5, (0, 5)),
        ([1, 6, 7, 2], 13, (1, 2)),
        ([9, 9], 18, (0, 1)),
        ([6, 4, 2, 8], 12, (1, 3)),
    ],
)
def test_pair_sum(numbers, target_sum, expected_result):
    assert pair_sum(numbers, target_sum) == expected_result
