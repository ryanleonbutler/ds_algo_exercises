import pytest

from ds_algo_exercises.compress import compress


@pytest.mark.parametrize(
    "uncompressed_string, expected_result",
    [
        ("ccaaatsss", "2c3at3s"),
        ("ssssbbz", "4s2bz"),
        ("ppoppppp", "2po5p"),
        ("nnneeeeeeeeeeeezz", "3n12e2z"),
        (
            "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",  # noqa
            "127y",
        ),
    ],
)
def test_compress(uncompressed_string, expected_result):
    assert compress(uncompressed_string) == expected_result
