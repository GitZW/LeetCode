"""
Given an image represented by an N x N matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

 

Example 1:

Given matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

Rotate the matrix in place. It becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

Rotate the matrix in place. It becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-matrix-lcci
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        len_matrix = len(matrix)
        if len_matrix == 1:
            return
        for row in range(len_matrix // 2):
            for col in range((len_matrix + 1) // 2):
                matrix[row][col], matrix[len_matrix - col - 1][row], matrix[len_matrix - row - 1][len_matrix - col - 1], \
                matrix[col][len_matrix - row - 1] \
                    = matrix[len_matrix - col - 1][row], matrix[len_matrix - row - 1][len_matrix - col - 1], \
                      matrix[col][len_matrix - row - 1], matrix[row][col]

        return matrix


class Solution2(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list, zip(*matrix[::-1]))
        return matrix


s = Solution()
print(s.rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
