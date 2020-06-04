"""
Implement a function to check if a binary tree is a binary search tree.

Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

Input:
    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: Input: [5,1,4,null,null,3,6].
     the value of root node is 5, but its right child has value 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/legal-binary-search-tree-lcci
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
