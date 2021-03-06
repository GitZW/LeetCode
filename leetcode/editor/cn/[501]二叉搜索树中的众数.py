# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。 
# 
#  假定 BST 有如下定义： 
# 
#  
#  结点左子树中所含结点的值小于等于当前结点的值 
#  结点右子树中所含结点的值大于等于当前结点的值 
#  左子树和右子树都是二叉搜索树 
#  
# 
#  例如： 
# 给定 BST [1,null,2,2], 
# 
#     1
#     \
#      2
#     /
#    2
#  
# 
#  返回[2]. 
# 
#  提示：如果众数超过1个，不需考虑输出顺序 
# 
#  进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内） 
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        tmp = collections.Counter(res).most_common()
        for k, v in tmp:
            if v == tmp[0][1]:
                ans.append(k)

        return ans
