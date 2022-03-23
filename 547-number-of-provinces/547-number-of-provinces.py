class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        N = len(isConnected)
        visited = [0 for _ in range(N)]
        
        def check(t):
            for k in range(N):
                if isConnected[t][k] and not visited[k]:
                    visited[k] = 1
                    check(k)
        
        for i in range(N):
            if not visited[i]:
                for j in range(N):
                    if isConnected[i][j]:
                        check(j)
                ans += 1
        
        
        return ans