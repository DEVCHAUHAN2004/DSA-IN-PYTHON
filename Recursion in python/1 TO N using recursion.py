
def func(i,n):
  if i > n:
    return
  print(i)
  func(i+1, n)

func(1,4)



# i = 1
# n = 10
# count = 0

# for i in range(n):
#   count +=1
#   print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
