nums = [0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 9]

def bubble_sort_already_sorted(nums):
    n = len(nums)
    for i in range(n - 1, 0, -1):   # pass from end to start
        is_swap = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swap = True
        if not is_swap:   # no swap → already sorted
            break
    return nums

print(bubble_sort_already_sorted(nums))
# [0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 9]