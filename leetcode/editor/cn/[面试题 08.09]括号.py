# 括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  例如，给出 n = 3，生成结果为： 
# 
#  
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#  
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def f(l, r, s):
            l == r == n and ans.append(s)
            l < n and f(l + 1, r, s + '(')
            r < l and f(l, r + 1, s + ')')

        f(0, 0, '')
        return ans
# leetcode submit region end(Prohibit modification and deletion)
