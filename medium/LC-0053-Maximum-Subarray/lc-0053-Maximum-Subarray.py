def maxSubArray(nums):
    maxSub = nums[0]
    curSum = 0  
    for num in nums:
        if curSum < 0:
            curSum = 0
        curSum += num
        maxSub = max(maxSub, curSum)
    return maxSub

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

