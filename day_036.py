"""
对于一组不同重量、不同价值，不可分割的物品，我们需要选择一些装入背包，在满足背包最大重量限制的前提下，背包中可装入物品的总价值最大是多少呢？
"""


class Solution(object):
    def max_price(self, weights, prices, weight_limit):
        """
        :type weights list  物品重量数组
        :type price list  物品价格
        :weight_limit  重量限制
        """
        if weight_limit <= 0:
            return 0
        if not weights:
            return 0
        if len(weights) != len(prices):
            return 0

        len_w = len(weights)
        # 下标代表重量 值代表这个重量对应最大价值 例如 status[0][2] =3, 表示第一个1个物品放入背包重量为2最大价值是3
        status = [[0] * (weight_limit + 1) for _ in range(len_w)]
        status[0][0] = 0
        if weights[0] <= weight_limit:
            status[0][weights[0]] = prices[0]

        for i in range(1, len_w):
            for j in range(0, weight_limit + 1):  # 不装第i个物品
                if status[i - 1][j] > 0:
                    status[i][j] = status[i - 1][j]

            for j in range(weight_limit + 1 - weights[i]):  # 装第i个物品
                status[i][j + weights[i]] = max(status[i - 1][j] + prices[i], status[i][j + i])

        print(status)
        return max([max(status[i]) for i in range(len(status))])


s = Solution()
w = [2, 2]
p = [3, 4]
print(s.max_price(w, p, 9))
