def has_duplicate(nums):
    my_set = set()
    for num in nums:
        if num in my_set:
            return True
        my_set.add(num)
    return False

nums_1 = [1,2,3,3]
nums_2 = [1,2,3,4]

print(has_duplicate(nums_1))
print(has_duplicate(nums_2))