# 5  20 3 
# 7  6  9 
# 1  4  6  
nums = [[5,20,3],[7,6,9],[1,4,7]]
# n = len(nums)

rows = len(nums)
columns = len(nums[0])

for i in range(0,rows):
  for j in range(0,columns):
    if i == j and i <= j and i>= j:
      print(nums[i][j],end=' ')
    else:
      print("*",end= ' ')   
  print()
# 5 * * 
# * 6 * 
# * * 7  

  