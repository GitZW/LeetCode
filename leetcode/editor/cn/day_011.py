"""
Implement an algorithm to find the kth to last element of a singly linked list. Return the value of the element.

Note: This problem is slightly different from the original one in the book.

Example:

Input:  1->2->3->4->5 和 k = 2
Output:  4
Note:

k is always valid.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        list_val = []
        while True:
            if head is not None:
                list_val.append(head.val)

            if head.next is None:
                break
            else:
                head = head.next

        return list_val[-k]


class Solution2:
    def kthToLast(self, head, k: int) -> int:
        fast = head
        slow = head
        while k > 0:
            fast = fast.next
            k -= 1
        while fast != None:
            fast = fast.next
            slow = slow.next
        return slow.val
