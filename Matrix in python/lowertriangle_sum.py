nums = [[5,20,3],[7,6,9],[1,4,6]]

rows = len(nums)
columns = len(nums[0])

lower_sum = 0
for i in range(rows):
    for j in range(columns):
        if i >= j:   # condition for upper triangle
            lower_sum += nums[i][j]

print("Lower Triangle sum =", lower_sum)
# Lower Triangle sum = 29