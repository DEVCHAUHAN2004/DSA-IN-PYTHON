nums = [[5,20,3],[7,6,9],[1,4,7]]

rows = len(nums)
columns = len(nums[0])

d_sum = 0
for i in range(rows):
    for j in range(columns):
        if i == j:   # main diagonal condition
            d_sum += nums[i][j]

print("Main diagonal sum =", d_sum)
# Main diagonal sum = 18
