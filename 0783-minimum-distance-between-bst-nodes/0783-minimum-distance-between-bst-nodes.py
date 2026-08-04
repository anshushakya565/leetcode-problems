# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.mini = float('inf')
        def helper(root):
            if root == None:
                return
            helper(root.left)
            if self.prev != None:
                self.mini = min(self.mini, root.val - self.prev)
            self.prev = root.val

            # li.append(root.val)
            helper(root.right)
        # li = []
        helper(root)
        # for i in range(len(li)):
        #     mini = min(mini, (li[i] + 1) - li[i])
        return self.mini