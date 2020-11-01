# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ] 
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res = []
        for i in range(numRows):
            r = [None] * (i + 1)
            r[0], r[-1] = 1, 1
            for j in range(1, i):
                r[j] = res[i-1][j-1] + res[i-1][j]

            res.append(r)
        return res

s=Solution()
s.generate(5)