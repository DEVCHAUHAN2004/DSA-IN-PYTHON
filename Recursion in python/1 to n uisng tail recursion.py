def func(i,n):
  if i > n:
    return
  func(i+1, n)
  print(i)

func(1,10)
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
