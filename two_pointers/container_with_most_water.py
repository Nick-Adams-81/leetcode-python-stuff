def maxArea(heights: list[int]) -> int:
    left = 0
    right = len(heights) -1
    result = 0
    while left < right:
        current_length = right - left
        if heights[left] < heights[right]:
            result = max(result, heights[left] * current_length)
            left += 1
        else:
            result = max(result, heights[right] * current_length)
            right -= 1
    return result