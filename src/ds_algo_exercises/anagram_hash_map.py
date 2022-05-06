def anagram(s1: str, s2: str) -> bool:
    """
    Checks if two string inputs are `anagrams` of each other.
    `Anagrams` are strings that contain the same characters, but in any order.

    Args:
        s1(str): First string in the input
        s2(str): Second string in the input

    Returns:
        bool: True or False
    """
    if len(s1) != len(s2):
        return False
    else:
        s1_map = {}
        for c in s1:
            s1_map[c] = s1.count(c)

        s2_map = {}
        for c in s2:
            s2_map[c] = s2.count(c)

        print(s1_map)
        print(s2_map)

        if s1_map == s2_map:
            return True
        else:
            return False
