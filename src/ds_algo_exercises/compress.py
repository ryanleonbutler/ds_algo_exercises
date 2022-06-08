def compress(s: str) -> str:
    """
    Returns compressed string.

    Args:
    s(str): uncompressed string e.g."aaa"

    Returns:
    str: compressed string e.g. "3a"
    """
    s += "#"
    result = []
    i = 0
    j = 0

    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            if num > 1:
                result.append(f"{num}{s[i]}")
            else:
                result.append(f"{s[i]}")
            i = j
            j += 1
            print(result)

    return "".join(result)
