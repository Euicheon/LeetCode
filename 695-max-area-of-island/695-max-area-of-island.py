class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        
        def dfs(r,c):
            if(0<= r < len(grid) and 0<= c < len(grid[0])
               and ((r,c) not in visited) and grid[r][c] != 0):
                visited.add((r,c))
                return (1 + dfs(r+1,c)+ dfs(r-1,c)+ dfs(r,c+1)+ dfs(r,c-1))
            return 0
        
        island = [0]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                temp = dfs(r,c)
                if temp:
                    island.append(temp)
        return max(island)