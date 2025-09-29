nums1 = [1,1,1,2,4,5,6,7]
nums2 = [1,2,3,6,7,8,9,10]

def merge_sorted_arrays_simple(nums1, nums2):
    return sorted(set(nums1 + nums2))

print(merge_sorted_arrays_simple(nums1, nums2))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]