"""
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

说明：解集不能包含重复的子集。

示例:

 输入： nums = [1,2,3]
 输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-set-lcci
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        cur_list = [[]]

        def _subsets(num, cur_l):
            copy = cur_l[:]
            for c in copy:
                cur_l.append(c+[num])

            return cur_l

        for num in nums:
            cur_list = _subsets(num, cur_list)

        return cur_list


test = [1,2,3]
s = Solution()
print(s.subsets(test))

# [[1], []]
# [[1, 2], [2], []]