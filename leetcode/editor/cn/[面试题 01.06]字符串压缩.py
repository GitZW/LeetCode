# 字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没
# 有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。 
# 
#  示例1: 
# 
#  
#  输入："aabcccccaaa"
#  输出："a2b1c5a3"
#  
# 
#  示例2: 
# 
#  
#  输入："abbccd"
#  输出："abbccd"
#  解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
#  
# 
#  提示： 
# 
#  
#  字符串长度在[0, 50000]范围内。 
#  
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)

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
# leetcode submit region end(Prohibit modification and deletion)
