# 满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。 
# 
#  返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。 
# 
#  答案中每个树的每个结点都必须有 node.val=0。 
# 
#  你可以按任何顺序返回树的最终列表。 
# 
#  
# 
#  示例： 
# 
#  输入：7
# 输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0
# ,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 解释：
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 20 
#  
#  Related Topics 树 递归


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    memo = {1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return
        if N not in Solution.memo:
            ans = []
            for x in range(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]
# leetcode submit region end(Prohibit modification and deletion)
