nums1 = [1,1,1,2,4,5,6,7]
nums2 = [1,2,3,6,7,8,9,10]

def mergetwo_sortedarrays_withoutduplicates(nums1, nums2):
    n = len(nums1)
    m = len(nums2)

    i = 0
    j = 0
    res = []

    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            if len(res) == 0 or res[-1] != nums1[i]:
                res.append(nums1[i])
            i += 1
        else:
            if len(res) == 0 or res[-1] != nums2[j]:
                res.append(nums2[j])
            j += 1

    while i < n:
        if len(res) == 0 or res[-1] != nums1[i]:
            res.append(nums1[i])
        i += 1

    while j < m:
        if len(res) == 0 or res[-1] != nums2[j]:
            res.append(nums2[j])
        j += 1

    return res

print(mergetwo_sortedarrays_withoutduplicates(nums1, nums2))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def merge_sorted_arrays(nums1, nums2):
#     return sorted(set(nums1) | set(nums2))


