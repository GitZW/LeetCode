"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

 

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zero-matrix-lcci
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_count = len(matrix)
        col_count = len(matrix[0])
        zero_row = set()
        zero_col = set()
        for row in range(row_count):
            for col in range(col_count):
                if matrix[row][col] == 0:
                    zero_row.add(row)
                    zero_col.add(col)

        for row in range(row_count):
            for col in range(col_count):
                if row in zero_row:
                    matrix[row][:] =[0]*col_count
                    break
                if col in zero_col:
                    matrix[row][col] = 0

        return matrix

s= Solution()
print(s.setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]))