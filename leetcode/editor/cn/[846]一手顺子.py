# 爱丽丝有一手（hand）由整数数组给定的牌。 
# 
#  现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。 
# 
#  如果她可以完成分组就返回 true，否则返回 false。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
# 输出：true
# 解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。 
# 
#  示例 2： 
# 
#  输入：hand = [1,2,3,4,5], W = 4
# 输出：false
# 解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= hand.length <= 10000 
#  0 <= hand[i] <= 10^9 
#  1 <= W <= hand.length 
#  
# 
#  
# 
#  注意：此题目与 1294 重复：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-co
# nsecutive-numbers/ 
#  Related Topics Ordered Map


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isNStraightHand(self, hand, W):
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in xrange(m, m+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1

        return True
# leetcode submit region end(Prohibit modification and deletion)
