# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看
# 做它自身的一棵子树。 
# 
#  示例 1: 
# 给定的树 s: 
# 
#  
#      3
#     / \
#    4   5
#   / \
#  1   2
#  
# 
#  给定的树 t： 
# 
#  
#    4 
#   / \
#  1   2
#  
# 
#  返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。 
# 
#  示例 2: 
# 给定的树 s： 
# 
#  
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
#  
# 
#  给定的树 t： 
# 
#  
#    4
#   / \
#  1   2
#  
# 
#  返回 false。 
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
