# 有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。 
# 
#  示例1: 
# 
#   输入：S = "qqe"
#  输出：["eqq","qeq","qqe"]
#  
# 
#  示例2: 
# 
#   输入：S = "ab"
#  输出：["ab", "ba"]
#  
# 
#  提示: 
# 
#  
#  字符都是英文字母。 
#  字符串长度在[1, 9]之间。 
#  
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return []

        result = [""]

        for i in S:
            result = self.add_char(i, result)
        return result

    def add_char(self, c, c_list):
        result = []
        list_copy = c_list.copy()

        for e in list_copy:
            for i in reversed(range(len(list(e)) + 1)):
                list_e = list(e)
                list_e.insert(i, c)
                new_str = "".join(list_e)
                if new_str not in result:
                    result.append(new_str)

        return result
