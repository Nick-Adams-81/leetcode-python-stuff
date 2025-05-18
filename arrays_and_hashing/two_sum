def two_sum(nums, target):
    # nums is a list of int
    # target is an int
    my_map = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in my_map:
            return [my_map[comp], i]
        my_map[num] = i
    return []


nums_1 = [3,4,5,6]
nums_2 = [4,5,6]

print(two_sum(nums_1, 7))
print(two_sum(nums_2, 10))