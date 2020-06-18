"""

三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13
提示:

n范围在[1, 1000000]之间
"""


class Solution(object):
    """
    内存和递归最大深度
    """
    def __init__(self):
        self.count_map = dict()

    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count_map[0] = 0
        self.count_map[1] = 1
        self.count_map[2] = 2
        self.count_map[3] = 4
        if n in self.count_map:
            return self.count_map[n]
        for i in range(4, n + 1):
            count = self.waysToStep(i - 1) + self.waysToStep(i - 2) + self.waysToStep(i - 3)
            self.count_map[i] = count % 1000000007
        return self.count_map[n]
