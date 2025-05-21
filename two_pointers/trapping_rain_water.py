def trap(height: list[int]) -> int:
    left, right = 0, len(height) -1
    maxLeft, maxRight = 0, 0
    result = 0
    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= maxLeft:
                maxLeft = height[left]
            else:
                result += maxLeft - height[left]
            left += 1
        else:
            if height[right] >= maxRight:
                maxRight = height[right]
            else:
                result += maxRight - height[right]
            right -= 1
    return result

heights = [0,2,0,3,1,0,1,3,2,1]
print(trap(heights))
