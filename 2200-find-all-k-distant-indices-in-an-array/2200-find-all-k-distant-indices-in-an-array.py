class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_idx_list = []
        visited = []
        N = len(nums)

        non_visited = [p for p in range(N)]
        for i in range(N):
            if nums[i] == key:
                key_idx_list.append(i)
                visited.append(i)
                non_visited.remove(i)
        for j in non_visited:
            for c in range(j-k,j+k+1):
                if(c in key_idx_list and j not in visited):
                    visited.append(j)
        # for t in key_idx_list:
        #     for j in range(t-k,t+k+1):
        #         if(j not in visited and j >= 0 and j<N):
        #             visited.append(j)
        visited.sort()
        return visited