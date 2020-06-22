# 给定一个布尔表达式和一个期望的布尔结果 result，布尔表达式由 0 (false)、1 (true)、& (AND)、 | (OR) 和 ^ (XOR)
#  符号组成。实现一个函数，算出有几种可使该表达式得出 result 值的括号方法。 
# 
#  示例 1: 
# 
#  输入: s = "1^0|0|1", result = 0
# 
# 输出: 2
# 解释: 两种可能的括号方法是
# 1^(0|(0|1))
# 1^((0|0)|1)
#  
# 
#  示例 2: 
# 
#  输入: s = "0&0&0&1^1|0", result = 1
# 
# 输出: 10 
# 
#  提示： 
# 
#  
#  运算符的数量不超过 19 个 
#  
#  Related Topics 栈 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countEval(self, s, result):
        """
        :type s: str
        :type result: int
        :rtype: int
        """
        self.ops = {
            '&': {
                True: [(True, True)],
                False: [(True, False), (False, True), (False, False)]
            },
            '|': {
                True: [(True, False), (False, True), (True, True)],
                False: [(False, False)]
            },
            '^': {
                True: [(True, False), (False, True)],
                False: [(True, True), (False, False)]
            }
        }

        return self._countEval(s, result)

    import functools
    @functools.lru_cache(None)
    def _countEval(self, s, result):

        if len(s) == 1:
            val = int(s)
            return int(bool(val) == result)

        total = 0
        for i in range(len(s)):
            if s[i] in self.ops:
                for bool_r, bool_l in self.ops[s[i]][result]:
                    total += self._countEval(s[:i], bool_r) * self._countEval(s[i + 1:], bool_l)

        return total


e = "1^0|0|1"
result = 0
s = Solution()
print(s.countEval(e, result))
