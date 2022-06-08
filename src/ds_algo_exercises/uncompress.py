def uncompress(s: str) -> str:
    """
    Returns uncompressed string.

    Args:
        s(str): string that needs be uncompressed e.g. "2c3a1t"

    Returns:
        str: uncompressed string e.g. "ccaaat"
    """
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[j].isnumeric():
            j += 1
        else:
            num = int(s[i:j:])
            result.append(s[j] * num)
            j += 1
            i = j

    return "".join(result)
