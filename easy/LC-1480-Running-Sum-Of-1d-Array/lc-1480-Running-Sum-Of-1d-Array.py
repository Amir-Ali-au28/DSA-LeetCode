def runningSum(nums):
    result = []
    
    for i in range(len(nums)):
        result.append(sum(nums[:i+1]))
    return result

nums = [1,2,3,4]
print(runningSum(nums))
