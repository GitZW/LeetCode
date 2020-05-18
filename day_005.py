"""
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

 

Example 1:

Input:
first = "pale"
second = "ple"
Output: True
Example 2:

Input:
first = "pales"
second = "pal"
Output: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/one-away-lcci
"""


class Solution(object):
    def _check_edits(self, first, second):
        diff_char_count = 0
        for index in range(len(first)):
            if first[index] != second[index]:
                diff_char_count += 1
                if diff_char_count > 1:
                    return False

        return True

    def _check_insert(self, first, second):
        if second.startswith(first):
            return True
        inert_char_count = 0
        for index in range(len(second)):
            if first[index - inert_char_count] != second[index]:
                inert_char_count += 1
                if inert_char_count > 1:
                    return False

        return True

    def oneEditAway(self, first, second):
        """
        :type first: str
        :type second: str
        :rtype: bool
        """
        len_first = len(first)
        len_second = len(second)
        if len_first == len_second:
            return self._check_edits(first, second)
        elif len_first - len_second == 1:
            return self._check_insert(second, first)
        elif len_second - len_first == 1:
            return self._check_insert(first, second)
        else:
            return False


class Solution2(object):
    def oneEditAway(self, first, second):
        """
        :type first: str
        :type second: str
        :rtype: bool
        """
        l1 = len(first)
        l2 = len(second)
        if l1 > l2:
            s1 = first
            s2 = second
        else:
            s1 = second
            s2 = first
        k = len(s2)
        for i in range(0, len(s2)):
            if s1[i] != s2[i]:
                k = i
                break

        return s1[k + 1:] == s2[k:] or s1[k + 1:] == s2[k + 1:]


s = Solution()
print(s.oneEditAway("pales", "pal"))
print(s.oneEditAway("pale", "pal"))
print(s.oneEditAway("pale", "pala"))
print(s.oneEditAway("", "a"))
