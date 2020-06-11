"""

设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角移动到右下角的路径。



网格中的障碍物和空位置分别用 1 和 0 来表示。

返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
解释:
输入中标粗的位置即为输出表示的路径，即
0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角）
说明：r 和 c 的值均不超过 100。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/robot-in-a-grid-lcci
"""


class Solution(object):
    """
    m 二位数组表示路径 ans[row-1][col-1]
    其中1表示可以到达，0表示不能到达
    ans[i][j] = max(ans[i-1][j],ans[i][j-1])
    """

    def pathWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if not obstacleGrid:
            return []

        ans = [[0] * col for _ in range(row)]
        # 检查是否可到达
        if obstacleGrid[0][0] == 1 or obstacleGrid[row - 1][col - 1] == 1:
            return []

        ans[0][0] = 1

        # 初始话ans 的第一行和第一列,避免求ans的时候数组越界
        for i in range(1, row):
            if obstacleGrid[i][0] == 0:
                ans[i][0] = ans[i - 1][0]
            else:
                ans[i][0] = 1

        for i in range(1, col):
            if obstacleGrid[0][i] == 0:
                ans[0][i] = ans[0][i - 1]
            else:
                ans[0][i] = 1

        # 求ans
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    ans[i][j] = 0
                else:
                    ans[i][j] = max(ans[i - 1][j], ans[i][j - 1])

        # 最后一个点不能到达
        if ans[-1][-1] == 0:
            return []

        result = []
        row_index = row - 1
        col_index = col - 1
        result.insert(0, [row_index, col_index])

        # 求路径
        while row_index > 0 or col_index > 0:
            c = col_index - 1

            if c >= 0 and ans[row_index][c] == 1:
                result.insert(0, [row_index, c])
                col_index = c
            else:
                row_index -= 1
                result.insert(0, [row_index, col_index])

        return result


test = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

s = Solution()
print(s.pathWithObstacles(test))
