def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) -1

    while left <= right:
        mid = left + ((right - left) // 2)
        if nums[mid] > target:
            right = mid -1
        elif nums[mid] < target:
            left = mid +1
        else:
            return mid
    return -1

nums = [-1,0,2,4,6,8]
print(search(nums, 4))