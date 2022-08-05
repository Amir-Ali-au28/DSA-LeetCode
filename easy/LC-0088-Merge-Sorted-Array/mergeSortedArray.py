def merge(nums1, m, nums2, n):
    if n > 0:
        p1 = m-1
        p2 = n-1
        k = (m+n)-1

        while k >= 0:
            if p1 < 0:
                nums1[k] = nums2[p2]
                p2 -= 1
            elif p2 < 0:
                nums1[k] = nums1[p1]
                p1 -= 1
            else:

                if nums1[p1] > nums2[p2]:
                    nums1[k] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[k] = nums2[p2]
                    p2 -= 1
            k -= 1
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1,m,nums2,n))