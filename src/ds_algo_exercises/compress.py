def compress(s: str) -> str:
    """
    Returns compressed string.

    Args:
    s(str): uncompressed string e.g."aaa" 

    Returns:
    str: compressed string e.g. "3a"
    """
    result = []
    i = 0
    j = 0
    
    while j < len(s):
        if (j != len(s) - 1) and s[j] == s[j+1]:
            j += 1
        else:
            j += 1
            num = len(s[i:j])
            if num > 1:
                result.append(f"{num}{s[j-1]}")
            else:
                result.append(f"{s[j-1]}")
            i = j
            print(result)

    return "".join(result)
