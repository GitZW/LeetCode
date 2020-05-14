"""

Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

Example 1:

Input: s = "leetcode"
Output: false
Example 2:

Input: s = "abc"
Output: true
 

Note:

0 <= len(s) <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-unique-lcci

"""


class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        return len(set(astr)) == len(astr)
