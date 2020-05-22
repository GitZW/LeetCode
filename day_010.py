"""
Write code to remove duplicates from an unsorted linked list.

Example1:

 Input: [1, 2, 3, 3, 2, 1]
 Output: [1, 2, 3]
Example2:

 Input: [1, 1, 1, 1, 2]
 Output: [1, 2]
Note:

The length of the list is within the range[0, 20000].
The values of the list elements are within the range [0, 20000].
Follow Up:

How would you solve this problem if a temporary buffer is not allowed?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-node-lcci
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
