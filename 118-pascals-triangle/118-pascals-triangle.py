class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        init = [1]
        if(numRows == 1): return [[1]]
        pascal.append(init)
        for i in range(1,numRows):
            temp = [1]
            # print(pascal)
            for j in range(1,i):
                temp.append(pascal[i-1][j-1]+pascal[i-1][j])
            temp.append(1)
            pascal.append(temp)
        return pascal