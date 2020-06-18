"""
给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

3
解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]
提示：

节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paths-with-sum-lcci
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.count = 0

    def check_sum(self, root, sum):
        if not root:
            return 0

        if root.val == sum:
            self.count += 1
        self.check_sum(root.right, sum - root.val)
        self.check_sum(root.left, sum - root.val)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.check_sum(root, sum)
        self.pathSum(root.right, sum)
        self.pathSum(root.left, sum)

        return self.count


class Solution2:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def f(r, s):
            if r:
                s = [i + r.val for i in s] + [r.val]
                return s.count(sum) + f(r.left, s) + f(r.right, s)
            return 0

        return f(root, [])
