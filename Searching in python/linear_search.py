nums = [5,3,9,8,1,6,4,10]
target = 6

def find_target_index(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1

index = find_target_index(nums, target)
print(index)  # Output: 5
