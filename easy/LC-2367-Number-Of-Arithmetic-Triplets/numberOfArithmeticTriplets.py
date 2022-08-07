class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        output = 0
        for i in range(len(nums)):
            temp2 = diff + nums[i]
            if temp2 in nums:
                temp3 = diff + temp2
                if temp3 in nums:
                    output += 1
        return output

