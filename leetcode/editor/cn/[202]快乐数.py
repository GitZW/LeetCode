# 编写一个算法来判断一个数 n 是不是快乐数。 
# 
#  「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为 1，那么这个数就是快乐数。 
# 
#  如果 n 是快乐数就返回 True ；不是，则返回 False 。 
# 
#  
# 
#  示例： 
# 
#  输入：19
# 输出：true
# 解释：
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#  
#  Related Topics 哈希表 数学


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        set_check = set()

        def check(n):
            count = sum([int(i) ** 2 for i in str(n)])
            if count == 1:
                return True
            if count in set_check:
                return False
            set_check.add(count)
            return check(count)

        return check(n)


s = Solution()
print(s.isHappy(19))
