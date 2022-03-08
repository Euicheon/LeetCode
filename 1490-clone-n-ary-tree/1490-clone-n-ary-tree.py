"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        newChildren = None
        if(root == None):
            return None
        if(root.children != None):
            newChildren = list(map(self.cloneTree,root.children))
        newRoot = Node(root.val, children=newChildren)
        return newRoot