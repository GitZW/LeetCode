"""

Given two strings,write a method to decide if one is a permutation of the other.

Example 1:

Input: s1 = "abc", s2 = "bca"
Output: true
Example 2:

Input: s1 = "abc", s2 = "bad"
Output: false
Note:

0 <= len(s1) <= 100
0 <= len(s2) <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-permutation-lcci
"""


class Solution(object):
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        for e in set(s1):
            if s1.count(e) != s2.count(e):
                return False

        return True
