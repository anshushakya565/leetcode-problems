# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root == None:
                return
            helper(root.left)
            li.append(root.val)
            helper(root.right)
        li = []
        helper(root)
        # is_sorted = all(li[i] <= li[i + 1] for i in range(len(li) - 1))
        # if is_sorted:
        if li == sorted(li) and len(li) == len(set(li)):
            return True
        return False
