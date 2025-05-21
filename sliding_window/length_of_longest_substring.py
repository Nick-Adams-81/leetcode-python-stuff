def longest(s: str) -> int:
    char_map = {}
    left = 0
    result = 0
    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        result = max(result, right - left + 1)
    return result

print(longest("zxyzxyz"))
print(longest("xxxx"))