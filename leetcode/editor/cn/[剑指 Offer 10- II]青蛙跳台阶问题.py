# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。 
# 
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。 
# 
#  示例 1： 
# 
#  输入：n = 2
# 输出：2
#  
# 
#  示例 2： 
# 
#  输入：n = 7
# 输出：21
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 100 
#  
# 
#  注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/ 
# 
#  
#  Related Topics 递归


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n + 1):
            self.f(i)

        return self.f(n) % 1000000007

    import functools
    @functools.lru_cache(maxsize=101)
    def f(self, n):
        if n>=3:
            return (self.f(n - 1) + self.f(n - 2))
        else:

            if n <= 0:
                return 1
            if n == 1:
                return 1
            elif n == 2:
                return 2


class Solution2:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


print(Solution().numWays(2))
