from collections import deque

def pivotIndex(nums):
    leftSum = 0
    rightSum = sum(nums)
    nums = deque(nums)
    nums.appendleft(0)
    
    for i in range(1,len(nums)):
        leftSum += nums[i-1]
        rightSum -= nums[i]
        if leftSum == rightSum:
            return i-1
    return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))



# Bruteforce approch

def pivotIndex1(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1

