# 设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整
# 个棋盘的那两条对角线。 
# 
#  注意：本题相对原题做了扩展 
# 
#  示例: 
# 
#   输入：4
#  输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#  解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#  
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []

        # pre_q下标表示行，value 表示列，下标从0 开始。列 col[0]=3 第1行第4列放皇后

        def put_q(i, n, pre_q):
            if i == n:
                ans.append(pre_q)

            for cow in range(n):
                if self.is_ok(pre_q, i, cow):
                    tmp = pre_q[:]
                    tmp.append(cow)
                    put_q(i + 1, n, tmp)

        put_q(0, n, [])
        return self.transResult(ans)

    def is_ok(self, done_list, rol, cow):
        for index, i in enumerate(done_list):
            if index == rol or i == cow or abs(rol - index) == abs(cow - i):
                return False
        return True

    def transResult(self, result):
        """
        :param result: [[1,3,4],[]]
        :return: [["..Q.","...Q"],[....]]
        """
        if not result:
            return []
        r = []
        len_q = len(result[0])
        for i in result:
            init_list = []
            for j in i:
                tmp = ["."] * len_q
                tmp[j] = "Q"
                init_list.append("".join(tmp))

            r.append(init_list)

        return r


s = Solution()
# print(s.transResult([[0, 1, 2, 3]]))
print(s.solveNQueens(4))
