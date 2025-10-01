nums = [[5,20,3],[7,6,9],[1,4,7]]

rows = len(nums)
columns = len(nums[0])

s_sum = 0
for i in range(rows):
    for j in range(columns):
        if i+j == rows - 1:   # main diagonal condition
            s_sum += nums[i][j]

print("Secondary diagonal sum =", s_sum)
# Secondary diagonal sum = 10
