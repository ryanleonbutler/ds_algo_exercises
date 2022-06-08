def most_frequent_char(s: str) -> str:
    char_map = dict.fromkeys(list(s), 0)

    for char in s:
        char_map[char] += 1

    result = max(char_map, key=char_map.get)

    return result
