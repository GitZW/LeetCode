# 给你一个整数 n，请你返回 任意 一个由 n 个 各不相同 的整数组成的数组，并且这 n 个数相加和为 0 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 5
# 输出：[-7,-1,1,3,4]
# 解释：这些数组也是正确的 [-5,-1,1,2,3]，[-3,-1,2,-2,4]。
#  
# 
#  示例 2： 
# 
#  输入：n = 3
# 输出：[-1,0,1]
#  
# 
#  示例 3： 
# 
#  输入：n = 1
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 1000 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        if n < 1:
            return []
        elif n == 1:
            return [0]
        else:
            if n % 2 == 1:
                ans = [0]
                n -= 1

            while n > 0:
                ans.extend([n, -n])
                n -= 2
        return ans
# leetcode submit region end(Prohibit modification and deletion)
