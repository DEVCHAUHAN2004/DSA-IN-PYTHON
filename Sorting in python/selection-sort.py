def selectionsort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:   # find the minimum
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]  # swap
    return nums

print(selectionsort([7,3,1,6,4,9,0,7,4,5,2,6]))
# [0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 9]