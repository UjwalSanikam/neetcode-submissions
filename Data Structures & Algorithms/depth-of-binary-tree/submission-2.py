# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        stack = []
        v = []
        max_depth = 1
        depth = 1
        temp = root
        stack.append(temp)
        while temp != None:
            if temp.left != None and temp.left not in v:
                temp = temp.left
                stack.append(temp)
                v.append(temp)
                depth = depth + 1
                if max_depth < depth:
                    max_depth = depth
            elif temp.right != None and temp.right not in v:
                temp = temp.right
                depth = depth + 1
                stack.append(temp)
                v.append(temp)
                if max_depth < depth:
                    max_depth = depth
            else:
                depth = depth - 1
                stack.pop()
                if len(stack) == 0:
                    break
                temp = stack[-1]
        return max_depth