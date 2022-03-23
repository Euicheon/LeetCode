from collections import defaultdict

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        print(len(workers),len(bikes))
        # min_w = [2500 for _ in range(len(workers))]
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                dist = abs(w[0]-b[0]) + abs(w[1]-b[1])
                dic[dist].append((i,j))
        dic = dict(sorted(dic.items()))
        # picked_w = [False for _ in range(len(workers))]
        picked_b = [False for _ in range(len(bikes))]
        ans = [-1 for _ in range(len(workers))]
        pc = 0
        # print(dic)
        for d in dic:
            for c in dic[d]:
                w,b = c
                if ans[w]==-1 and not picked_b[b]:
                    # picked_w[w] = True
                    picked_b[b] = True
                    ans[w] = b
                    pc += 1
                    if(pc == len(workers)):
                        return ans
        return ans