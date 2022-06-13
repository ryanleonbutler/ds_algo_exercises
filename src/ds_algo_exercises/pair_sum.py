from typing import List, Tuple


def pair_sum(numbers: List, target_sum: int) -> Tuple:
    j = 0
    k = 0

    for i in range(len(numbers) - 1):
        k = 0
        for n in range(len(numbers) - 1):
            k += 1
            if numbers[j] + numbers[k] == target_sum:
                return (j, k)
        j += 1
