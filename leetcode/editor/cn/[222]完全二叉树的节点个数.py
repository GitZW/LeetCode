# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。 
# 
#  完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层
# 为第 h 层，则该层包含 1~ 2h 个节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,2,3,4,5,6]
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目范围是[0, 5 * 104] 
#  0 <= Node.val <= 5 * 104 
#  题目数据保证输入的树是 完全二叉树 
#  
# 
#  
# 
#  进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？ 
#  Related Topics 树 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.countNodes(root.right) + self.countNodes(root.left) + 1


# leetcode submit region end(Prohibit modification and deletion)


# 对于最大层数为 hh 的完全二叉树，节点个数一定在 [2^h,2^{h+1}-1]的范围内，可以在该范围内通过二分查找的方式得到完全二叉树的节点个数。

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        level = 0
        node = root.left
        while node:  # 这里获得层数
            level += 1
            node = node.left
        l = 1 << level  # 左界
        r = (l << 1) - 1  # 右界

        while l < r:
            mid = int((r + l + 1) / 2)  # 中位
            node = root
            path = 1 << (level - 1)  # 取mid号数的后几位的模板
            while node and path > 0:
                if mid & path:
                    node = node.right
                else:
                    node = node.left
                path >>= 1  # 一层查完，查下一层
            if node:
                l = mid  # 存在left位置变化
            else:
                r = mid - 1  # 不存在right位置变化
        return r
