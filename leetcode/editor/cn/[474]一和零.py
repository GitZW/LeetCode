# 在计算机界中，我们总是追求用有限的资源获取最大的收益。 
# 
#  现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。 
# 
#  你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。 
# 
#  注意: 
# 
#  
#  给定 0 和 1 的数量都不会超过 100。 
#  给定字符串数组的长度不会超过 600。 
#  
# 
#  示例 1: 
# 
#  
# 输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# 输出: 4
# 
# 解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
#  
# 
#  示例 2: 
# 
#  
# 输入: Array = {"10", "0", "1"}, m = 1, n = 1
# 输出: 2
# 
# 解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j] i表示可用0的个数， j表示可用的1的个数
        # dp[i][j] = max(dp[i][j], 1 + dp[i - item_count0][j - item_count1])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            count_0, count_1 = self._get_number_of_0_1(s)
            for i in range(m, count_0 - 1, -1):
                for j in range(n, count_1 - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - count_0][j - count_1])
        print(dp)
        return dp[m][n]

    def _get_number_of_0_1(self, str):
        return str.count("0"), str.count("1")


m = 5
n = 3
Array = {"10", "0001", "111001", "1", "0"}
s = Solution()
print(s.findMaxForm(Array, m, n))
