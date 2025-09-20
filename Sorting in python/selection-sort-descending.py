def selectionsort(nums):
    n = len(nums)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if nums[j] > nums[max_index]:   # find the minimum
                max_index = j
        nums[i], nums[max_index] = nums[max_index], nums[i]  # swap
    return nums

print(selectionsort([7,3,1,6,4,9,0,7,4,5,2,6]))
# [9, 7, 7, 6, 6, 5, 4, 4, 3, 2, 1, 0]