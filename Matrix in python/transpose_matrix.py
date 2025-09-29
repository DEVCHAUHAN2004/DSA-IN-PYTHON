nums = [[5,20,3],
        [7,6,9],
        [1,4,7]]

rows = len(nums)
columns = len(nums[0])

# Create empty transpose matrix
transpose = [[0] * rows for _ in range(columns)]

for i in range(rows):
    for j in range(columns):
        transpose[j][i] = nums[i][j]

print("Transpose of the matrix:")
for row in transpose:
    print(row)

# [5, 7, 1]
# [20, 6, 4]
# [3, 9, 7]