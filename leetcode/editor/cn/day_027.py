"""
设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。

例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]

    3
   / \
  5   1
 / \ / \
6  2 0  8
  / \
 7   4
示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-common-ancestor-lcci
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        if root == p or root == q:
            return root

        if self.find_node(root.left, p):
            if self.find_node(root.right, q):
                return root
            else:
                return self.lowestCommonAncestor(root.left, p, q)
        else:
            if self.find_node(root.left, q):
                return root
            else:
                return self.lowestCommonAncestor(root.right, p, q)

    def find_node(self, root, target_node):
        if not root:
            return False

        if root == target_node:
            return True

        found = self.find_node(root.left, target_node)
        if found:
            return True
        found = self.find_node(root.right, target_node)

        return found


class Solution2(object):
    """
    假设我们从跟结点开始，采用 DFS 向下遍历，如果当前结点到达叶子结点下的空结点时，返回空；如果当前结点为 p 或 q 时，返回当前结点；

    这样，当我们令 left = self.lowestCommonAncestor(root.left, p, q) 时，如果在左子树中找到了 p 或 q，left 会等于 p 或 q，同理，right 也是一样；

    然后我们进行判断：如果 left 为 right 都不为空，则为情况 1；如果 left 和 right 中只有一个不为空，说明这两个结点在子树中，则根节点到达子树再进行寻找。

    """
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        right = self.lowestCommonAncestor(root.right, p, q)
        left = self.lowestCommonAncestor(root.left,p,q)

        if right and left:
            return root
        else:
            return left or right
