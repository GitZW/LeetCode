"""
递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。

示例1:

 输入：A = 1, B = 10
 输出：10
示例2:

 输入：A = 3, B = 4
 输出：12
提示:

保证乘法范围不会溢出

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recursive-mulitply-lcci
"""


class Solution(object):
    def __init__(self):
        self.result = dict()

    def multiply(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        if not A or not B:
            return 0

        if self.result.get(B):
            return self.result[B]

        if B == 1:
            return A

        for i in range(1, B + 1):
            self.result[i] = self.multiply(A, i // 2) + self.multiply(A, i - i // 2)

        return self.result[B]


s = Solution()
print(s.multiply(13231, 0))
