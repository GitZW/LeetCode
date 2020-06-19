# 硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007) 
# 
#  示例1: 
# 
#  
#  输入: n = 5
#  输出：2
#  解释: 有两种方式可以凑成总金额:
# 5=5
# 5=1+1+1+1+1
#  
# 
#  示例2: 
# 
#  
#  输入: n = 10
#  输出：4
#  解释: 有四种方式可以凑成总金额:
# 10=10
# 10=5+5
# 10=5+1+1+1+1+1
# 10=1+1+1+1+1+1+1+1+1+1
#  
# 
#  说明： 
# 
#  注意: 
# 
#  你可以假设： 
# 
#  
#  0 <= n (总金额) <= 1000000 
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def __init__(self):
        self.sum_ways = 0

    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 1:
            return 0

        def change(n, coins):
            if n < 0:
                return
            if not coins:
                return
            if n == 0:
                self.sum_ways += 1

            ## 区分使用coins[0] 和不使用coins[0]
            change(n - coins[0], coins)
            if n >= coins[1]:
                change(n, coins[1:])

        change(n, [1, 5, 10, 25])
        return self.sum_ways


# leetcode submit region end(Prohibit modification and deletion)

class Solution2(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """

        d = [0] * (n + 1)
        d[0] = 1

        coins = [1, 5, 10, 25]
        # 先使用小额硬币，避免（1，1，5） （5，1，1）这种的重复组合
        for coin in coins:
            for i in range(coin, n + 1):
                d[i] += d[i - coin]

        return d[n] % 1000000007


s = Solution2()
print(s.waysToChange(5))
