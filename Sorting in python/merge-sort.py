def merge_array(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    
    mid = n // 2
    left_arr = nums[:mid]
    right_arr = nums[mid:]
    
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    
    return merge_array(left, right)

# Example usage
arr = [5, 3, 8, 4, 2,6,9,12,4,6,8,4,9,3,5,7,8]
sorted_arr = merge_sort(arr)
print(sorted_arr)
