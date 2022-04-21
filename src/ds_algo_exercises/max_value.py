from typing import List

def max_value(nums: List) -> int:
    largest = nums[0] 

    for num in nums:
        if num > largest:
            largest = num 

    return largest
