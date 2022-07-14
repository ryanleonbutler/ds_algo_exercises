from typing import List


def intersection(list_a: List, list_b: List) -> List:
    new_list = []

    set_b = set(list_b)

    for num in list_a:
        if num in set_b:
            new_list.append(num)

    return sorted(new_list)
