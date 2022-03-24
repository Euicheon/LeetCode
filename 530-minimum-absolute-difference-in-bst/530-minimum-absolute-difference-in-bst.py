# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        # global _min
        temp = []
        def bfs(proot):
            temp.append(proot.val)
            if(proot.left):
                bfs(proot.left)
            if(proot.right):
                bfs(proot.right)
        bfs(root)
        
        temp = sorted(temp)
        abs_temp = []
        for i in range(len(temp)-1):
            abs_temp.append(temp[i+1]-temp[i])
        
        return min(abs_temp)