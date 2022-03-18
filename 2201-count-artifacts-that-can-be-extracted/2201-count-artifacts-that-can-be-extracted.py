class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        ans = 0
        islands = {}
        remained_size = {}
        for i in range(len(artifacts)):
            (r1,c1,r2,c2) = artifacts[i]
            island = [0 for _ in range((r2+1-r1)*(c2+1-c1))]
            cnt = 0
            for x in range(r1,r2+1):
                for y in range(c1,c2+1):
                    islands[(x,y)] = i
                    cnt+=1
            remained_size[i] = cnt
        for d in dig:
            if tuple(d) in islands:
                id = islands[tuple(d)]
                remained_size[id] -= 1
                if(remained_size[id] == 0):
                    ans += 1
        #     label = d[0]+1+d[1]*n
        #     for island in islands:
        #         if label in island:
        #             island.remove(label)
        # ans =islands.count([])
        return ans