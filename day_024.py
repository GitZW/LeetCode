"""
Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.


Example 1:

Given tree [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
return true.
Example 2:

Given [1,2,2,3,3,null,null,4,4]
      1
     / \
    2   2
   / \
  3   3
 / \
4   4
return false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-balance-lcci
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def get_depth(self, root):
        if not root:
            return 0

        depth = max(self.get_depth(root.right), self.get_depth(root.left))

        return depth + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if not self.isBalanced(root.left):
            return False

        if not self.isBalanced(root.right):
            return False

        if abs(self.get_depth(root.right) - self.get_depth(root.left)) > 1:
            return False

        return True


class Solution2:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        if self.DeepTree(pRoot) == -1:
            return False
        else:
            return True

    def DeepTree(self, pRoot):
        if not pRoot:
            return 0
        left = self.DeepTree(pRoot.left)
        right = self.DeepTree(pRoot.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
