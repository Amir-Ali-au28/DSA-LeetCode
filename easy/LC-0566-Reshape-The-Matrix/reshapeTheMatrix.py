class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        r2 = len(mat)
        c2 = len(mat[0])
        
        if r2 * c2 != r * c:
            return mat
        
        arr = []
        
        for row in mat:
            for ele in row:
                arr.append(ele)
        
        idx = 0
        result = []
        
        for i in range(r):
            temp = []
            for i in range(c):
                temp.append(arr[idx])
                idx += 1
            result.append(temp)
        return result

