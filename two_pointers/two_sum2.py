def two_sum(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) -1
    while left < right:
        total = nums[left] + nums[right]
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            return [left +1, right +1]
    return []

numbers = [1,2,3,4]
print(two_sum(numbers, 3))
