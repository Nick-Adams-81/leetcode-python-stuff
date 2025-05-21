def longestConsecutive(nums: list) -> int:
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num -1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

numbers = [0,3,2,5,4,6,1,1]
print(longestConsecutive(numbers))