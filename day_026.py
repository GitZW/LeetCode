"""
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree.

Return null if there's no "next" node for the given node.

Example 1:

Input: root = [2,1,3], p = 1

  2
 / \
1   3

Output: 2
Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /
1

Output: null

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/successor-lcci
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.found = False
        self.last_node = None

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        if root.right:
            self.inorderSuccessor(root.right, p)
        if self.found:
            return self.last_node

        if root == p:
            self.found = True
            return self.last_node
        self.last_node = root

        if root.left:
            self.inorderSuccessor(root.left, p)
        if self.found:
            return self.last_node

        return self.last_node
