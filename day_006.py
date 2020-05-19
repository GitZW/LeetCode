"""
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

Example 1:

Input: "aabcccccaaa"
Output: "a2b1c5a3"
Example 2:

Input: "abbccd"
Output: "abbccd"
Explanation:
The compressed string is "a1b2c2d1", which is longer than the original string.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compress-string-lcci
"""


class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return S
        current_char = S[0]
        current_char_count = 0
        result = []
        for c in S:
            if current_char == c:
                current_char_count += 1
            else:
                result.append("".join([current_char, str(current_char_count)]))

                current_char = c
                current_char_count = 1

        result.append("".join([current_char, str(current_char_count)]))

        cs = "".join(result)

        return S if len(cs) >= len(S) else cs
