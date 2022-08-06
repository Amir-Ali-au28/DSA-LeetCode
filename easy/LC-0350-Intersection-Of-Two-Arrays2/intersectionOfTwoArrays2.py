class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                output.append(nums2[i])
                nums1.remove(nums2[i])
        
        return output

