import pytest

from ds_algo_exercises.uncompress import uncompress


@pytest.mark.parametrize(
    "s, expected_result",
    [
        ("2c3a1t", "ccaaat"),
        ("4s2b", "ssssbb"),
        ("2p1o5p", "ppoppppp"),
        ("3n12e2z", "nnneeeeeeeeeeeezz"),
        (
            "127y",
            "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",  # noqa
        ),
    ],
)
def test_uncompress_string(s, expected_result) -> None:
    assert isinstance(s, str)
    assert uncompress(s) == expected_result
