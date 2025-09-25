def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]          # element to be inserted
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
nums = [7, 3, 1, 6, 4, 9, 0, 7]
sorted_nums = insertion_sort(nums)
print(sorted_nums)
# [0, 1, 3, 4, 6, 7, 7, 9]
