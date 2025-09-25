def bubblesort(nums):
  n = len(nums)
  for i in range(n-2,-1,-1):
    for j in range(0,i+1):
      if nums[j] > nums[j+1]:
        nums[j], nums[j+1] = nums[j+1], nums[j]
  return nums       

print(bubblesort([7,3,1,6,4,9,0,7,4,5,2,6]))
# [0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 9]
