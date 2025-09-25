nums = [3, 4, 6, 8, 9, 10, 15]

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        print(False)
        break
else:
    print(True)




nums = [3, 4, 6, 8, 7, 10, 15]  # 8 > 7, not sorted

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        print(False)
        break
else:
    print(True)
