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
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    就是判断中序遍历后面一个值大于前面一个值
    """
    def __init__(self):
        self.last_visited = float("-inf")

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        flag = True
        if not root:
            return True

        if root.left:
            flag = self.isValidBST(root.left)
        if not flag:
            return False

        if root.val < self.last_visited:
            return False
        self.last_visited = root.val

        if root.right:
            flag = self.isValidBST(root.right)

        return flag
