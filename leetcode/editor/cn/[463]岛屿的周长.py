# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。 
# 
#  网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。 
# 
#  岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿
# 的周长。 
# 
#  
# 
#  示例 : 
# 
#  输入:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
# 
# 输出: 16
# 
# 解释: 它的周长是下面图片中的 16 个黄色的边：
# 
# 
#  
#  Related Topics 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def islandPerimeter(self, grid):
        """
        中间无湖，则 周长 = （上边+右边）*2
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        row_count = len(grid)
        col_count = len(grid[0])

        for row_index in range(row_count):
            for col_index in range(col_count):
                if grid[row_index][col_index] == 1:

                    if row_index == 0 or grid[row_index - 1][col_index] == 0:
                        ans += 1
                    # if row_index == row_count-1 or grid[row_index + 1][col_index] == 0:
                    #     ans += 1
                    # if col_index == 0 or grid[row_index][col_index - 1] == 0:
                    #     ans += 1
                    if col_index == col_count - 1 or grid[row_index][col_index + 1] == 0:
                        ans += 1

        return ans * 2


s = Solution()
grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]

print(s.islandPerimeter(grid))
