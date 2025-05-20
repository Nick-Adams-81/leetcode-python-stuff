def topKFrequentElements(nums: list[int], k: int) -> list:
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) +1)]
    for num, freq in freq_map.items():
        buckets[freq].append(num)

    result = []
    for i in range(len(buckets) -1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
            
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequentElements(nums, k))

