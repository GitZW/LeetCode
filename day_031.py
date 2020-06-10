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
    def pathWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])


class Solution:
    def pathWithObstacles(self, obstacleGrid):
        ans, r, c = [], len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[-1][-1] != 0:
            return ans
        obstacleGrid[-1][-1] = 2
        for i in reversed(range(r)):
            for j in reversed(range(c)):
                if obstacleGrid[i][j] > 1:
                    if i > 0 and not obstacleGrid[i - 1][j]:
                        obstacleGrid[i - 1][j] = 2
                    if j > 0 and not obstacleGrid[i][j - 1]:
                        obstacleGrid[i][j - 1] = 3
        if obstacleGrid[0][0] > 1:
            i, j = 0, 0
            while i < r and j < c:
                ans.append([i, j])
                if obstacleGrid[i][j] == 2:
                    i += 1
                else:
                    j += 1
        return ans