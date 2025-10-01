nums = [[5,20,3],[7,6,9],[1,4,6]]

rows = len(nums)
columns = len(nums[0])

upper_sum = 0
for i in range(rows):
    for j in range(columns):
        if j >= i:   # condition for upper triangle
            upper_sum += nums[i][j]

print("Upper Triangle sum =", upper_sum)
# Upper Triangle sum = 49