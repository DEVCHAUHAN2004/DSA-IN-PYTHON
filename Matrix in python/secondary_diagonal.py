# Matrix definition
nums = [[5,20,3],
        [7,6,9],
        [1,4,7]]

rows = len(nums)
columns = len(nums[0])

print("Secondary diagonal of the matrix:")
for i in range(rows):
    for j in range(columns):
        if i + j == rows - 1:   # condition for secondary diagonal
            print(nums[i][j], end=' ')
        else:
            print('*', end=' ')
    print()
# * * 3 
# * 6 *
# 1 * *