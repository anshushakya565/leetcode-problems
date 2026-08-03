# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        d = deque([[root, 1]])
        while d:
            node, depth = d.popleft() 
            if node.left == None and node.right == None:
                return depth
            if node.left:
                d.append([node.left, depth + 1])
            if node.right:
                d.append([node.right, depth + 1])
        return depth
