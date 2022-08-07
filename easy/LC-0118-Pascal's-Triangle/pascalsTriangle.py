class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for i in range(1,numRows+1):
            temp = []
            for j in range(i):
                if j == 0 or j == i-1:
                    temp.append(1)
                else:
                    val = result[i-2][j-1] + result[i-2][j]
                    temp.append(val)
            result.append(temp)
        
        return result

