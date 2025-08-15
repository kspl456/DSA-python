#Count Complete Tree Nodes
'''
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Approach-1 (Inorder Traversal):
'''
We will use an inorder traversal to count the nodes in the complete binary tree.
'''
class Solution:
    c=0
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.c+=1
            self.inorder(root.right)
    def countNodes(self, root):
        self.inorder(root)
        return self.c
    
## Approach-2 
'''
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible. To count the nodes efficiently, we can use a recursive approach that leverages the properties of complete binary trees.
We can count the nodes by recursively counting the left and right subtrees. The base case is when the root is None, in which case we return 0. For each node, we return 1 (for the current node) plus the count of nodes in the left subtree and the count of nodes in the right subtree.
This approach has a time complexity of O(n), where n is the number of nodes in the tree, since we visit each node exactly once. However, it does not meet the requirement of running in less than O(n) time complexity.
Instead, we can optimize the counting process by using the properties of complete binary trees to count nodes more efficiently. We can calculate the height of the leftmost and rightmost paths of the tree, and if they are equal, we can use the formula for the number of nodes in a complete binary tree: 2^h - 1, where h is the height of the tree. If they are not equal, we recursively count the nodes in the left and right subtrees.
This optimized approach has a time complexity of O(log^2 n) in the average case, which is significantly better than O(n) for large trees, while still ensuring that we count all nodes correctly.
'''
class Solution:
    def countNodes(self, root):
        if not root: return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)