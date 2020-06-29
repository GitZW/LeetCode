# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。 
# 
#  
# 
#  例如: 
# 给定二叉树: [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 1000 
#  
# 
#  注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-tra
# versal/ 
#  Related Topics 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        queue = []
        queue.append((root, 0))
        while queue:
            c_node, depth = queue.pop()
            if c_node.left:
                queue.insert(0, (c_node.left, depth + 1))
            if c_node.right:
                queue.insert(0, (c_node.right, depth + 1))

            if depth >= len(ans):
                ans.append([])

            ans[depth].append(c_node.val)
        return ans


class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        queue = []
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                c_node = queue.pop()
                tmp.append(c_node.val)

                if c_node.left:
                    queue.insert(0, c_node.left)
                if c_node.right:
                    queue.insert(0, c_node.right)

            ans.append(tmp)

        return ans
