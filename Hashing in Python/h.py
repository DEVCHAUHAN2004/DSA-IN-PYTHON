n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]

freq = {}

for num in n:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# print frequency table
for key, val in freq.items():
    print(f"{key} → {val}")

