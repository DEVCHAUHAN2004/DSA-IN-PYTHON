# n = int(input("Enter the number: "))
# res = []

# for i in range(1,n+1):
#   if n % i == 0:
#     res.append(i)
# print(res)

nums = int(input("Enter the number: "))
res = []
x = nums // 2
for i in range(1,x):
  if nums % i == 0:
    res.append(i)
res.append(nums)

print(res)




