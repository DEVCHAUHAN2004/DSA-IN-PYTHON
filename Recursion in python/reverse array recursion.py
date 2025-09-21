def reversearray(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    reversearray(nums, left+1, right-1)

nums = [5, 4, 2, 6, 8, 1, 2, 3, 9, 4, 7, 1, 7, 5, 4, 2, 8, 7]

print("Original:", nums)
reversearray(nums, 0, len(nums)-1)
print("Reversed:", nums)
# Original: [5, 4, 2, 6, 8, 1, 2, 3, 9, 4, 7, 1, 7, 5, 4, 2, 8, 7]
# Reversed: [7, 8, 2, 4, 5, 7, 1, 7, 4, 9, 3, 2, 1, 8, 6, 2, 4, 5]

