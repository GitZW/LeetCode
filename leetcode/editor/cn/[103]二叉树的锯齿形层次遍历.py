# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。 
# 
#  例如： 
# 给定二叉树 [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回锯齿形层次遍历如下： 
# 
#  [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#  Related Topics 栈 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ans = []
        stack = [root]
        is_right_from = True # 是否右往左遍历

        while stack:
            node_val_list = []
            for i in range(len(stack)):
                cur = stack.pop()
                node_val_list.append(cur.val)
                cur.left and stack.insert(0, cur.left)
                cur.right and stack.insert(0, cur.right)
            ans.append(node_val_list) if is_right_from else  ans.append(node_val_list[::-1])
            is_right_from = not is_right_from

        return ans

