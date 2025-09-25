nums = [55, 32, -98, 65, 80, 98, 34, 23]

largest = float("-inf")
s_largest = float("-inf")

# Find the largest
for i in range(len(nums)):
  if nums[i] > largest:
    s_largest = largest
    largest = nums[i]

  elif nums[i] > s_largest and nums[i] != largest:
    s_largest = nums[i]
      
print(s_largest)
# 80

