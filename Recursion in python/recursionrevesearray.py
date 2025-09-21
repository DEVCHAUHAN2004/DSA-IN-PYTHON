def reverse(arr):
    if len(arr) == 0:
        return []
    return [arr[-1]] + reverse(arr[:-1])

arr = [1,2,3,4,5,6,7,8,9,10]
print(reverse(arr))

# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
