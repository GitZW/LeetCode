"""
Given a sorted (increasing order) array with unique integer elements, write an algo­rithm to create a binary search tree with minimal height.

Example:

Given sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5]，which represents the following tree:

          0
         / \
       -3   9
       /   /
     -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-height-tree-lcci
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        len_nums = len(nums)

        if len_nums == 1:
            return TreeNode(nums[0])

        mid_index = len_nums//2
        root = TreeNode(nums[mid_index])
        root.left = self.sortedArrayToBST(nums[0:mid_index])
        root.right = self.sortedArrayToBST(nums[mid_index+1:])

        return root


