class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        if len(items1) < len(items2):
            items1, items2 = items2, items1
        
        items1Value = {}
        items2Value = {}
        ret = {}
        idx = []
        output = []
        
        for i in range(len(items1)):
            key = items1[i][0]
            val= items1[i][1]
            items1Value[key] = val
            
        for i in range(len(items2)):
            key = items2[i][0]
            val= items2[i][1]
            items2Value[key] = val
        
        for k in items1Value:
            if k in items2Value:
                ret[k] = items1Value[k] + items2Value[k]
                idx.append(k)
            else:
                ret[k] = items1Value[k]
                idx.append(k)
                
        for k in items2Value:
            if k in ret:
                pass
            else:
                ret[k] = items2Value[k]
                idx.append(k)
                
        idx.sort()
        
        for i in idx:
            temp = []
            temp.append(i)
            temp.append(ret[i])
            output.append(temp)
        
        return output


