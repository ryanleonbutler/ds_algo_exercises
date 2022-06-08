def anagrams(s1: str, s2: str) -> bool:
    """
    Checks if two string inputs are `anagrams` of each other.
    `Anagrams` are strings that contain the same characters, but in any order.

    Args:
        s1(str): First string in the input
        s2(str): Second string in the input

    Returns:
        bool: True or False
    """
    s1_map = char_map(s1)
    s2_map = char_map(s2)
    if s1_map == s2_map:
        return True
    else:
        return False


def char_map(s):
    count = {}

    for char in s:
        if char not in count:
            count[char] = 0

        count[char] += 1

    return count
