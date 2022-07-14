from typing import List


def intersection(list_a: List, list_b: List) -> List:
    new_list = []

    for j in list_a:
        for k in list_b:
            if j == k:
                new_list.append(j)

    return sorted(new_list)
