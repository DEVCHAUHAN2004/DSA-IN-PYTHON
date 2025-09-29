nums = [[5,20,3],[1,-10,9],[1,4,6]]

rows = len(nums)       # 3 rows
columns = len(nums[0]) # 3 columns

for i in range(rows):         
    row_sum = 0
    for j in range(columns): 
        row_sum += nums[i][j]
    print("Row", i, "sum =", row_sum)
# Row 0 sum = 28
# Row 1 sum = 0
# Row 2 sum = 11

nums = [[5,20,3],[1,-10,9],[1,4,6]]

rows = len(nums)       # 3 rows
columns = len(nums[0]) # 3 columns

for j in range(columns):         
    column_sum = 0
    for i in range(rows): 
        column_sum += nums[i][j]
    print("Columns", j, "sum =", column_sum)
# Columns 0 sum = 7
# Columns 1 sum = 14
# Columns 2 sum = 18

