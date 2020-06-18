"""
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

 

Example:

Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
Follow Up: Suppose the digits are stored in forward order. Repeat the above problem.

Example:

Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-lists-lcci
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur_node = ListNode(-1)
        head.next = cur_node
        overflow = 0
        while l1 or l2 or overflow:
            if not l1:
                l1 = ListNode(0)

            if not l2:
                l2 = ListNode(0)

            node_num = (l1.val + l2.val + overflow) % 10
            overflow = (l1.val + l2.val + overflow) // 10

            cur_node.next = ListNode(node_num)
            cur_node = cur_node.next

            l1 = l1.next
            l2 = l2.next

        return head.next


l1 = ListNode(7)
l1.next = ListNode(1)
l1.next.next = ListNode(6)

l2 = ListNode(5)
l2.next = ListNode(9)
l2.next.next = ListNode(2)

s = Solution()
print(s.addTwoNumbers(l1, l2).val)
