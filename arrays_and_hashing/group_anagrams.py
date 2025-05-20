from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list)
    for s in strs:
        sorted_word = tuple(sorted(s))
        result[sorted_word].append(s)
    return list(result.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(words))