def isAnagram(s, t):
    if len(s) != len(t):
        return False
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    for num in count:
        if num != 0:
            return False
    return True

str_1 = "racecar"
str_2 = "carrace"

str_3 = "jar"
str_4 = "jam"

print(isAnagram(str_1, str_2))
print(isAnagram(str_3, str_4))