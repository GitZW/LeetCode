"""
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 (e.g.,"waterbottle" is a rotation of"erbottlewat"). Can you use only one call to the method that checks if one word is a substring of another?

Example 1:

Input: s1 = "waterbottle", s2 = "erbottlewat"
Output: True
Example 2:

Input: s1 = "aa", "aba"
Output: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-rotation-lcci
"""


class Solution(object):
    def isFlipedString(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False

        find = (s2 + s2).rfind(s1)
        if find < 0:
            return False

        flip_count = len(s1) - find

        if s1[:flip_count] == s2[find:] and s1[flip_count:] == s2[:find]:
            return True

        return False


class Solution2:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s1 in s2 * 2


s = Solution()
print(s.isFlipedString("waterbottle", "erbottlewat"))
