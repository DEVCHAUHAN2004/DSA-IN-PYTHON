n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 1, 9, 5, 2, 6, 8, 7]

# hash list based on max value
hash_list = [0] * (max(n) + 1)

# build frequency hash
for num in n:
    hash_list[num] += 1

# queries
for num in m:
    if num < 1 or num > max(n):
        print(0)
    else:
        print(hash_list[num])


