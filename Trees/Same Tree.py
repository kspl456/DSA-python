#Same Tree
'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    
'''
# Approach:
1. Base Case: If both nodes are None, they are the same (return True).
2. If one node is None and the other is not, they are not the same (return False).
3. If the values of the current nodes are not equal, return False.
4. Recursively check the left and right subtrees:
   - Call the function for the left children of both trees.
   - Call the function for the right children of both trees.
5. If both recursive calls return True, then the trees are the same; otherwise, they are not.

Time Complexity: O(n), where n is the number of nodes in the trees. We visit each node exactly once.
Space Complexity: O(h), where h is the height of the tree, due to the recursion stack.
'''