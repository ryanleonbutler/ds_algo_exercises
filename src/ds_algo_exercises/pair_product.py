def pair_product(numbers, target_product):
    previous_nums = {}

    for index, num in enumerate(numbers):
        complement = target_product / num

        if complement in previous_nums:
            return (previous_nums[complement], index)

        previous_nums[num] = index
