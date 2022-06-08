import pytest

from ds_algo_exercises.most_frequent_char import most_frequent_char


@pytest.mark.parametrize(
    "s, expected_result",
    [
        ("bookeeper", "e"),
        ("david", "d"),
        ("abby", "b"),
        ("mississippi", "i"),
        ("potato", "o"),
        ("eleventennine", "e"),
        ("riverbed", "r"),
    ],
)
def test_most_frequent_char(s, expected_result):
    assert most_frequent_char(s) == expected_result
