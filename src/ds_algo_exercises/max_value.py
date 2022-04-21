from typing import List

def max_value(nums: List) -> int:
    largest = nums[0]

    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]

    return largest
