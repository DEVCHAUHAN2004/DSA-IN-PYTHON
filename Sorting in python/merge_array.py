left = [1,2,3,4,5]
right = [1,2,3,4,5,6,7,8,9]

def merge_array(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    while i < n:
        result.append(left[i])
        i += 1

    while j < m:
        result.append(right[j])
        j += 1

    return result  # Correct indentation

# Test
print(merge_array(left, right))
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]