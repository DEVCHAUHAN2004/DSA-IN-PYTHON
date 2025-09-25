left = [10, 25, 17, 33, 21]
right = [12, 22, 31, 18, 43, 56, 32, 9, 90]

# Sort the arrays first
left.sort()
right.sort()

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

    return result

# Test
print(merge_array(left, right))
# [9, 10, 12, 17, 18, 21, 22, 25, 31, 32, 33, 43, 56, 90]