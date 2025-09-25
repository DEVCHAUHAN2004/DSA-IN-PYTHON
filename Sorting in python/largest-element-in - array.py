nums = [55, 32, -98, 65, 80, 98, 34, 23]

largest = nums[0]       # initialize with first element
for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]

print(largest)
# 98

nums = [55, 32, -98, 65, 80, 98, 34, 23]

largest = nums[0]  # initialize with the first element
n = len(nums)

for i in range(1, n):
    largest = max(largest, nums[i])  # update largest if current element is bigger

print(largest)
