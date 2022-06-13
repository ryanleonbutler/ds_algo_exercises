from typing import List, Tuple


def pair_sum(numbers: List, target_sum: int) -> Tuple:
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return (i, j)
