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
    chars_s1 = sorted(list(s1))
    chars_s2 = sorted(list(s2))
    print(chars_s1, chars_s2, sep="\n")

    if len(chars_s1) != len(chars_s2):
        return False
    else:
        if chars_s1 == chars_s2:
            return True
        else:
            return False
