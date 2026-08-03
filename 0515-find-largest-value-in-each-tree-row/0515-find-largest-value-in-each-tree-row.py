# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        d = deque([root])
        ans = []
        while d:
            li = []
            for i in range(len(d)):
                node = d.popleft()
                li.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            ans.append(max(li))
        return ans