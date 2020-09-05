# 给定一个二叉树，计算整个树的坡度。 
# 
#  一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。 
# 
#  整个树的坡度就是其所有节点的坡度之和。 
# 
#  
# 
#  示例： 
# 
#  输入：
#          1
#        /   \
#       2     3
# 输出：1
# 解释：
# 结点 2 的坡度: 0
# 结点 3 的坡度: 0
# 结点 1 的坡度: |2-3| = 1
# 树的坡度 : 0 + 0 + 1 = 1
#  
# 
#  
# 
#  提示： 
# 
#  
#  任何子树的结点的和不会超过 32 位整数的范围。 
#  坡度的值不会超过 32 位整数的范围。 
#  
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            right_val = dfs(root.right)
            left_val = dfs(root.left)
            ans += abs(right_val - left_val)
            return root.val + right_val+left_val
        dfs(root)
        return ans


