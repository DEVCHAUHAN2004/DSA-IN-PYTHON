nums = [55, 32, -98, 65, 80, 98, 34, 23]

largest = float("-inf")
s_largest = float("-inf")

# Find the largest
for i in range(len(nums)):
    largest = max(largest, nums[i])

# Find the second largest
for i in range(len(nums)):
    if nums[i] != largest and nums[i] > s_largest:
        s_largest = nums[i]

print(s_largest)
# 80