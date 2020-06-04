"""
Given a string, write a function to check if it is a permutation of a palin­ drome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

 

Example1:

Input: "tactcoa"
Output: true（permutations: "tacocat"、"atcocta", etc.）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation-lcci
"""


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        odd_char = 0
        checked_char = set()
        for e in s:
            if e not in checked_char and s.count(e) % 2 != 0:
                odd_char += 1
                if odd_char > 1:
                    return False
                else:
                    checked_char.add(e)
        return True


s = Solution()
print((s.canPermutePalindrome("")))
