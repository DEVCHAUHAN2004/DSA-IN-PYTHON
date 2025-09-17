nums = [5,6,7,7,1,9,9,1,1,5,4,7,6,9,2,4,6,7]
n = len(nums)
freq_map = {}

for i in range(n):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1   # <-- Use = here

print(freq_map)

