nums = [4, 1, 7, 6, 3, 2, 8]

def partition(nums, low, high):
    pivot = nums[low]
    i, j = low, high

    while i < j:
        while i <= high and nums[i] <= pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return j

def quick_sort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        quick_sort(nums, low, p_index - 1)
        quick_sort(nums, p_index + 1, high)

quick_sort(nums, 0, len(nums) - 1)
print(nums)
# [1, 2, 3, 4, 6, 7, 8]
