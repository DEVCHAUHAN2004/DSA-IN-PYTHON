nums = [1,1,1,2,3,4,4,7,9,9,9,10]

n = len(nums)
freq_map = {}

# store unique numbers in freq_map
for i in range(n):
    freq_map[nums[i]] = 0   # assignment, not comparison

j = 0
for k in freq_map:
    nums[j] = k
    j += 1

print(j)      # number of unique elements
print(nums[:j])  # unique elements
# 7
# [1, 2, 3, 4, 7, 9, 10]