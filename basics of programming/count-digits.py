# n = int(input("Enter the number: "))
# num = n
# count = 0
# while num > 0:
#   count += 1
#   num = num // 10
# print(count)


num = 12345
count = len(str(num))
print("Number of digits:", count)


import math
num = 1234567578
count = int(math.log10(num)) + 1
print("Number of digits:", count)


