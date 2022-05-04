import pytest

from ds_algo_exercises.anagram import anagram


@pytest.mark.parametrize(
    "s1, s2, expected_result",
    [
        ("restful", "fluster", True),
        ("cats", "tocs", False),
        ("monkeyswrite", "newyorktimes", True),
        ("paper", "reapa", False),
        ("elbow", "below", True),
        ("tax", "taxi", False),
        ("taxi", "tax", False),
        ("night", "thing", True),
        ("abbc", "aabc", False),
    ],
)
def test_anagram(s1, s2, expected_result):
    assert anagram(s1, s2) == expected_result
