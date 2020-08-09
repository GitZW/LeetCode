# 给定一个未经排序的整数数组，找到最长且连续的的递增序列，并返回该序列的长度。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 
#  
# 
#  示例 2: 
# 
#  输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。
#  
# 
#  
# 
#  注意：数组长度不会超过10000。 
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cul_lcis = 1
        ans = []
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cul_lcis += 1
            else:
                ans.append(cul_lcis)
                cul_lcis = 1
        ans.append(cul_lcis)

        return max(ans)


s = Solution()
s.findLengthOfLCIS([1, 3, 5, 4, 5, 6, 7, 8])
