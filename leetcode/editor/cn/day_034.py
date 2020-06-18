"""
对于一组不同重量、不可分割的物品，我们需要选择一些装入背包，在满足背包最大重量限制的前提下，背包中物品总重量的最大值是多少呢？
"""


class Solution(object):
    def max_weight(self, weights, weight_limit):
        """
        :type weights list  物品重量数组
        :weight_limit  重量限制
        """
        if weight_limit <= 0:
            return 0
        if not weights:
            return 0

        # 下标代表重量 值代表这个重量和能否装进背包 例如 status[1] =True,表示背包能放进重量1
        status = [False] * (weight_limit + 1)
        status[0] = True
        if weights[0] <= weight_limit:
            status[weights[0]] = True

        for i in range(len(weights)):
            for j in reversed(range(weight_limit + 1 - weights[i])):
                if status[j]:
                    status[weights[i] + j] = True

        for i in reversed(range(weight_limit + 1)):
            if status[i]:
                return i

        return 0


s = Solution()
print(s.max_weight([2, 2, 4, 6, 3], 9))
