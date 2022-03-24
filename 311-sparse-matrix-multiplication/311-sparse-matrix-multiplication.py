class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat2)
        n = len(mat2[0])
        # print(m,k,n)
        ans = [[0 for i in range(n)] for j in range(m)]
        # print(ans)
        for i in range(m):
            for l in range(n):
                for j in range(k):
                    ans[i][l] += mat1[i][j]*mat2[j][l]
        
        return ans