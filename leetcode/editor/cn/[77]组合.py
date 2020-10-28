# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
import itertools


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(itertools.combinations(range(1,n+1),k))


class Solution2(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, n + 1)]

        res = []

        def backtrace(nums_b, curr_res, index):
            # print("curr_res:",curr_res)
            if len(curr_res) == k:
                res.append(curr_res[:])
                return

            for i in range(index, n):
                curr_res.append(nums[i])
                backtrace(nums_b[index:], curr_res, i + 1)
                curr_res.pop()

        if n == 0 or k == 0:
            return res

        backtrace(nums, [], 0)
        return res
