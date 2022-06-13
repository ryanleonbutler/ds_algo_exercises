from typing import List, Tuple


def pair_sum(numbers: List, target_sum: int) -> Tuple:
    previous_nums = {}

    for index, num in enumerate(numbers):
        print(index, num)
        complement = target_sum - num

        if complement in previous_nums:
            return (previous_nums[complement], index)

        previous_nums[num] = index
