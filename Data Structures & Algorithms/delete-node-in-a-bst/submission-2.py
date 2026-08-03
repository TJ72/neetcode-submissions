# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                minValueNode = self.findMinValueNode(root.right)
                root.val = minValueNode.val
                root.right = self.deleteNode(root.right, minValueNode.val)
        
        return root
    
    def findMinValueNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr and curr.left:
            curr = curr.left
        
        return curr